#Python3 automation Script for EVE-NG emulated Cisco Network.
#Basic static NAT
#See the topology in topology.jpg

#Import needed module and configuration arrays
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import commands as conf

#Define function to bypass initial configuration
def bypass_initial_config(prompt,conn):
	if "[yes/no]" in prompt or "initial configuration" in prompt or "please answer" in prompt:
		conn.send_command_timing("no\n")
		prompt = conn.find_prompt()
		print ('Bypassing Initial Configuration' + prompt)

#Define main() function
def main():
	with open('port.txt') as ports:
		for p in ports:

			p = p.strip()

			rtr = {
				'device_type' : 'cisco_ios_telnet',
				'ip' : '192.168.88.200',
				'port' : p
			}

			try:
				conn = ConnectHandler(**rtr)

			except (NetmikoTimeoutException, NetmikoAuthenticationException) as ex:
				print(ex)

			print("Connecting to 192.168.88.200:"+p)

			prompt = conn.find_prompt()

			bypass_initial_config(prompt,conn)

			if p == "32769":
				conn.enable('enable')
				conn.config_mode('conf t')
				print(conn.send_config_set(conf.cnfR1))
				print(conn.send_command('write'))

			else:
				conn.enable('enable')
				conn.config_mode('conf t')
				print(conn.send_config_set(conf.cnfR2))
				print(conn.send_command('write'))

			print ("Disconnecting from 192.168.88.200:"+p)
			conn.disconnect()



#Run main() function as main
if __name__ == "__main__":
	main()

