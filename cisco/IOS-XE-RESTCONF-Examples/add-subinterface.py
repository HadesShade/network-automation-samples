import restconf_lib as lib

# Enable the parent interface first
def enable_parent(auth):
    parentURL = "https://192.168.50.1/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/shutdown"
    return lib.deleteConfig(parentURL, auth)

def main():
    ip = "192.168.50.1"
    url = "https://192.168.50.1/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"
    data = {
        "2.10" : {
            "Cisco-IOS-XE-native:GigabitEthernet" : {
                "name" : "2.10",
                "description" : "CONTROLLER",
                "encapsulation" : {
                    "dot1Q" : {
                        "vlan-id" : "10"
                    }
                },
                "ip" : {
                    "address" : {
                        "primary" : {
                            "address" : "192.168.10.1",
                            "mask" : "255.255.255.0"
                        }
                    },

                    "Cisco-IOS-XE-nat:nat": {
                        "inside": [
                            None
                        ]
                    }
                }
            }
        },

        "2.20" : {
            "Cisco-IOS-XE-native:GigabitEthernet" : {
                "name" : "2.20",
                "description" : "ERP",
                "encapsulation" : {
                    "dot1Q" : {
                        "vlan-id" : "20"
                    }
                },
                "ip" : {
                    "address" : {
                        "primary" : {
                            "address" : "192.168.20.1",
                            "mask" : "255.255.255.0"
                        }
                    }
                }
            }
        }
    }

    auth = ("hq-adm","hq-adm")

    print (enable_parent(auth))

    for i in data:
        newurl = url + f"={i}"
        print (lib.setConfig(newurl, auth, data[i]))
    
    print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
    main()