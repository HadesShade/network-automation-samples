import restconf_lib as lib

auth = ("ro-adm","ro-adm")

url = "https://172.16.10.20/restconf/data/Cisco-IOS-XE-native:native/interface/Tunnel=1"

print (lib.getConfig(url, auth))