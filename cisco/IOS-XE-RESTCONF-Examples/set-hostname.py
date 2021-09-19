import restconf_lib as lib

auth = ("ro-adm","ro-adm")
ip = "172.16.10.20"
url = "https://172.16.10.20/restconf/data/Cisco-IOS-XE-native:native/hostname"
data = {
    "hostname" : "RO-MAIN"
}

print (lib.setConfig(url, auth, data))
print ("\n")
print (lib.saveConfig(auth, ip))