import restconf_lib as lib

def noShutdown(ip, auth, intNum):
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={intNum}/shutdown"
    return lib.deleteConfig(url, auth)

def ipv4Config(ip, auth, intNum, address, mask, description):
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet={intNum}"
    data = {
        "Cisco-IOS-XE-native:GigabitEthernet" : {
            "description" : description,
            "ip" : {
                "address" : {
                    "primary" : {
                        "address" : address,
                        "mask" : mask
                    }
                }
            }
        }
    }

    return lib.setConfig(url, auth, data)

def main() :
     ip = "172.16.10.20"
     auth = ("ro-adm","ro-adm")

     print (noShutdown(ip, auth, 3))
     print (ipv4Config(ip, auth, 3, "192.168.10.1", "255.255.255.0", "TO-ISP"))
     print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
    main()