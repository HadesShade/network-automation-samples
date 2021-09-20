import restconf_lib as lib

def configNetwork(ip, mask, area):
    data = {
        "ip" : ip,
        "mask" : mask,
        "area" : area
    }

    return data

def configOSPF(ip, auth, proID, roID, network):
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/router/ospf={proID}"
    data = {
    "Cisco-IOS-XE-ospf:ospf": {
        "id": proID,
        "log-adjacency-changes": {},
        "router-id": roID,
        "network": network
        }
    }

    return lib.createConfig(url, auth, data)

def main():
    ip = "192.168.50.1"
    auth = ("hq-adm","hq-adm")

    networks = {
        "1" : {
            "ip" : "192.168.10.0",
            "mask" : "0.0.0.255",
            "area" : 1
        },

        "2" : {
            "ip" : "192.168.20.0",
            "mask" : "0.0.0.255",
            "area" : 1
        },        

        "3" : {
            "ip" : "192.168.50.0",
            "mask" : "0.0.0.255",
            "area" : 1
        },

        "4" : {
            "ip" : "10.0.0.0",
            "mask" : "0.0.0.31",
            "area" : 0
        }
    }

    nlist = []

    for n in networks:
        nlist.append(configNetwork(networks[n]["ip"], networks[n]["mask"], networks[n]["area"]))
    
    print (configOSPF(ip, auth, 10, "11.11.11.11", nlist))
    print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
    main()