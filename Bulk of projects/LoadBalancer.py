import socket,sys,select,random,os,select,collections
from Logger import *

def openConfigurationFile():
	listServers = dict()
	file = open("/etc/rtrtr-lb.conf","r")
	servers = file.read().splitlines()
	for server in servers:
		ip = str(server.split(':')[0])
		port = int(server.split(':')[1])
		listServers[ip] = port
	LogInfo(f"Backend Servers Loaded : {listServers}")
	return listServers

def initializeFlowsCount():
	fCounts = dict()
	listServers = openConfigurationFile()
	for ip in listServers:
		fCounts[ip] = 0
	LogInfo(f"Initialize Connection Count for Every Backend Server : {fCounts}")
	return fCounts

flowsCount = initializeFlowsCount()
flowsPair = dict()
all_sockets = list()

def leastConn():
	connectionCount = list()
	choosenServers = list()
	choosenPorts = list()
	sortedCount = collections.OrderedDict(flowsCount)
	for server in sortedCount:
		connectionCount.append(int(sortedCount[server]))
		choosenServers.append(str(server))
		choosenPorts.append(int(openConfigurationFile()[server]))

	return connectionCount, choosenServers, choosenPorts

def startLB():
	listenSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listenSocket.bind(("0.0.0.0",9001))
	listenSocket.listen()
	all_sockets.append(listenSocket)

	while True:
		socket_readlist, socket_writelist, socket_exceptionlist = select.select(all_sockets, [], [])
		for sock in socket_readlist:
			if sock == listenSocket:
				onConnectionAccept(listenSocket)
				break

			else:
				data = sock.recv(4096)
				if data:
					onDataReceive(sock, data)
				else:
					onConnectionClose(sock)
					break

def onConnectionAccept(listenSocket):
	client_socket, client_ip = listenSocket.accept()
	server_connections, server_ips, server_ports = leastConn()
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	for i in range (len(server_connections)):
		if i == len(server_connections) - 1:
			try:
				server_socket.connect((server_ips[i],server_ports[i]))
				all_sockets.append(client_socket)
				all_sockets.append(server_socket)
				flowsPair[client_socket] = server_socket
				flowsPair[server_socket] = client_socket
				flowsCount[server_ips[i]] += 1
				LogInfo(f"Established Connection from {client_socket.getpeername()[0]} to {server_ips[i]}")
				break
			except Exception:
				LogError("No Connection to Backend Servers can be Established")
				client_socket.close()
		else:
			try:
				server_socket.connect((server_ips[i],server_ports[i]))
				all_sockets.append(client_socket)
				all_sockets.append(server_socket)
				flowsPair[client_socket] = server_socket
				flowsPair[server_socket] = client_socket
				flowsCount[server_ips[i]] += 1
				LogInfo(f"Established Connection from {client_socket.getpeername()[0]} to {server_socket.getpeername()[0]}")
				break
			except Exception:
				LogError(f"Connection to {server_ips[i]} failed. Trying next server ...")
				continue

def onDataReceive(client_socket, data):
	flowsPair[client_socket].send(data)

def onConnectionClose(socket):
	socket_pair = flowsPair[socket]
	pair_ip1 = socket.getpeername()[0]
	pair_ip2 = socket_pair.getpeername()[0]
	all_sockets.remove(socket)
	all_sockets.remove(socket_pair)

	socket.close()
	socket_pair.close()

	del flowsPair[socket]
	del flowsPair[socket_pair]

	if pair_ip1 in flowsCount:
		flowsCount[pair_ip1] -=1

	elif pair_ip2 in flowsCount:
		flowsCount[pair_ip2] -=1

	else:
		pass

	LogInfo(f"Connection from {pair_ip1} to {pair_ip2} terminated gracefully.")

if __name__ == "__main__":
	try:
		if sys.argv[1] == "start":
			startLB()
		elif sys.argv[1] == "stop":
			exit()
		else:
			print("Usage : LoadBalancer.py <start|stop>")

	except NameError:
		print("Usage : LoadBalancer.py <start|stop>")
