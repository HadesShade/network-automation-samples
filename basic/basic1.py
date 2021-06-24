# Basic Automation Python 3 Script for cisco using telnet for EVE-NG simulator.
# 2 Routers with 2 Clients. Connected with default static route.
# By : Hades Shade.
# Install netmiko first by "pip3 install netmiko"


# Import ConnectHandler from netmiko.
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

# Open file port.txt which contain port numbers for telnet
with open('port.txt') as ports:

	# Add device identity for each port
	# cisco_ios_telnet means device type is cisco_ios and we connect to it with telnet
	# 192.168.88.200 is the IP address of EVE-NG server.
	# p is numbers listed in ports.txt
	for p in ports:
		#remove trailing spaces and new lines from p value
		p = p.strip()

		router = {
			'device_type': 'cisco_ios_telnet',
			'ip': '192.168.88.200',
			'port': p
		}


		#Connect to routers using identity above
		try:
			conn = ConnectHandler(**router)

		except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
			print(error)

		#Show the current router which is ConnectHandler try to connect
		print ("Connecting to 192.168.88.200:"+p)

		# Telnet port 32769 is for R1 router.
		if p == "32769":

			prompt = conn.find_prompt()

			# Bypass initial configuration prompt
			if "[yes/no]" in prompt or 'initial configuration' in prompt or 'please answer' in prompt:
				conn.send_command_timing("no\n")
				prompt = conn.find_prompt()
				print ('Bypassing Initial Configuration' + prompt)

			#Enter privileged exec mode from user exec mode
			conn.enable('enable')

			#Enter Global Configuration Mode
			conn.config_mode('conf t')

			# Define Global Configuration Mode commands set.
			# Commands defined here will run sequentially.
			cmd = [
				'hostname R1',
				'int e0/0',
				'ip addr 10.0.0.1 255.255.255.252',
				'no sh',
				'exit',
				'int e0/1',
				'ip addr 192.168.10.1 255.255.255.0',
				'no sh',
				'exit',
				'ip route 0.0.0.0 0.0.0.0 10.0.0.2',
				'end'
			]

			# Execute above commands set in the Global Configuration Mode
			out = conn.send_config_set(cmd)
			print(out)

			# Send command to Privileged Exec Mode to save the configuration
			conn.send_command('write')

		# Same as R1 router, but this one is for R2 router (telnet port 32770)
		elif p == "32770":

			prompt = conn.find_prompt()

			# Bypass initial configuration prompt
			#if "[yes/no]" in prompt or 'initial configuration' in prompt or 'please answer' in prompt:
			#	conn.send_command_timing("no\n")
			#	prompt = conn.find_prompt()
			#	print ('Bypassing Initial Configuration' + prompt)

			conn.enable('enable')
			conn.config_mode('conf t')

			cmd = [
				'hostname R2',
				'int e0/0',
				'ip addr 10.0.0.2 255.255.255.252',
				'no sh',
				'exit',
				'int e0/1',
				'ip addr 192.168.20.1 255.255.255.0',
				'no sh',
				'exit',
				'ip route 0.0.0.0 0.0.0.0 10.0.0.1',
				'end'
			]

			out = conn.send_config_set(cmd)
			print(out)

			conn.send_command('write')

		conn.disconnect()
