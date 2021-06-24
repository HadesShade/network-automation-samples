from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

router = {
		'device_type':'cisco_ios_telnet',
		'ip':'192.168.88.200',
		'port':'32769'
}

conn = ConnectHandler(**router)

conn.find_prompt()
conn.enable('enable')
conn.config_mode('conf t')
out = conn.send_config_set('hostname R1')
print(out)
conn.disconnect()


