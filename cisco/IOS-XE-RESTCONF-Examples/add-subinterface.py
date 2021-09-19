import restconf_lib as lib

# Enable the parent interface first
def enable_parent(auth):
    parentURL = "https://172.16.10.20/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/shutdown"
    return lib.deleteConfig(parentURL, auth)

def main():
    ip = "172.16.10.20"
    url = "https://172.16.10.20/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"
    data = {
        "2.10" : {
            "Cisco-IOS-XE-native:GigabitEthernet" : {
                "name" : "2.10",
                "description" : "VLAN-10",
                "encapsulation" : {
                    "dot1Q" : {
                        "vlan-id" : "10"
                    }
                },
                "ip" : {
                    "address" : {
                        "primary" : {
                            "address" : "10.10.10.1",
                            "mask" : "255.255.255.0"
                        }
                    }
                }
            }
        },

        "2.20" : {
            "Cisco-IOS-XE-native:GigabitEthernet" : {
                "name" : "2.20",
                "description" : "VLAN-20",
                "encapsulation" : {
                    "dot1Q" : {
                        "vlan-id" : "20"
                    }
                },
                "ip" : {
                    "address" : {
                        "primary" : {
                            "address" : "10.20.20.1",
                            "mask" : "255.255.255.0"
                        }
                    }
                }
            }
        }
    }

    auth = ("ro-adm","ro-adm")

    print (enable_parent(auth))

    for i in data:
        newurl = url + f"={i}"
        print (lib.createConfig(newurl, auth, data[i]))
    
    print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
    main()