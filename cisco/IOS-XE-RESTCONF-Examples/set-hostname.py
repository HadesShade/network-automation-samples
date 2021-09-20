import restconf_lib as lib

auth = ("hq-adm","hq-adm")
ip = "192.168.50.1"
url = "https://192.168.50.1/restconf/data/Cisco-IOS-XE-native:native/hostname"
data = {
    "hostname" : "HQ-MAIN"
}

print (lib.setConfig(url, auth, data))
print ("\n")
print (lib.saveConfig(auth, ip))