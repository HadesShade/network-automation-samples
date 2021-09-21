import restconf_lib as lib

def addCommunity(name, access):

    data = {
        "name": name,
        access: [
          None
        ]
    }

    return data

def snmpHost(ip,  com, ver):
    data = {
        "ip-address": ip,
        "community-or-user": com,
        "version": ver
    }

    return data

def sendSNMPConfig(ip, auth, community, enable, host):
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/snmp-server"
    data = {
        "Cisco-IOS-XE-native:snmp-server": {
            "Cisco-IOS-XE-snmp:community": community,
             "Cisco-IOS-XE-snmp:enable": {
                "enable-choice": {
                    enable: {}
                }
             },
             "Cisco-IOS-XE-snmp:host": host
        }
    }

    return lib.createConfig(url, auth, data)

def main():
    ip = "192.168.50.1"
    auth = ("hq-adm", "hq-adm")

    community_dict = {
        "1" : {
            "name" : "COMPANY",
            "access" : "RO"
        }
    }
    comList =[addCommunity(community_dict[i]["name"], community_dict[i]["access"]) for i in community_dict]

    host_dict = {
        "1" : {
            "ip" : "192.168.10.10",
            "com" : "COMPANY",
            "ver" : "2c"
        }
    }

    hostList =[snmpHost(host_dict[i]["ip"], host_dict[i]["com"], host_dict[i]["ver"]) for i in host_dict]

    print (sendSNMPConfig(ip, auth, comList, "traps", hostList))
    print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
    main()






