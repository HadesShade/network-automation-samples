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
     ip = "192.168.50.1"
     auth = ("hq-adm","hq-adm")

     print (noShutdown(ip, auth, 1))
     print (ipv4Config(ip, auth, 1, "202.107.7.2", "255.255.255.252", "TO-ISP"))
     print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
    main()