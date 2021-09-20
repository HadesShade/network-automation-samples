import restconf_lib as lib

def addPATOverload(ip, auth, sourceList, interfaceName):
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/ip/nat"
    data = {
        "Cisco-IOS-XE-nat:nat": {
            "inside": {
                "source": {
                    "list": [
                        {
                            "id": sourceList,
                            "interface": [
                                {
                                    "name": interfaceName,
                                    "overload": [
                                        None
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }

    return lib.createConfig(url, auth, data)                                         

def main():
    ip = "192.168.50.1"
    auth = ("hq-adm","hq-adm")
    print (addPATOverload(ip, auth, "NAT", "GigabitEthernet1"))
    print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
    main()