import restconf_lib as lib

auth = ("hq-adm","hq-adm")

url = "https://192.168.50.1/restconf/data/Cisco-IOS-XE-native:native/snmp-server"

print (lib.getConfig(url, auth))