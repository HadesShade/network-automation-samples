#Python3 automation Script for EVE-NG emulated Cisco Network.
#Basic OSPF routing + DHCP Service
#See the topology in topology.jpg

from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

#Import configuration arrays
import commands as conf

#Bypass initial configuration prompt
def bypass(prompt):
	if "[yes/no]" in prompt or 'initial configuration' in prompt or 'please answer' in prompt:
		conn.send_command_timing("no\n")
		prompt = conn.find_prompt()
		print ('Bypassing Initial Configuration' + prompt)


#port.txt define all port numbers used for telnet connections to routers.
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
		bypass(prompt)


		if p == "32769":
			conn.enable('enable')
			conn.config_mode('conf t')
			glb = conn.send_config_set(conf.cfgR1)
			print(glb)
			print(conn.send_command('write'))

		elif p == "32770":
			conn.enable('enable')
			conn.config_mode('conf t')
			glb = conn.send_config_set(conf.cfgR2)
			print(glb)
			print(conn.send_command('write'))

		elif p == "32771":
			conn.enable('enable')
			conn.config_mode('conf t')
			glb = conn.send_config_set(conf.cfgR3)
			print(glb)
			print(conn.send_command('write'))

		else:
			conn.enable('enable')
			conn.config_mode('conf t')
			glb = conn.send_config_set(conf.cfgR4)
			print(glb)
			print(conn.send_command('write'))

	conn.disconnect()



