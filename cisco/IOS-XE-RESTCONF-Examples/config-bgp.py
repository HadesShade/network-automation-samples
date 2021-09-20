import restconf_lib as lib
import json

def addBGPNeighbor(ip, asnum):
    neighdata = {
        "id": ip,
        "remote-as": asnum
    }

    return neighdata

def configBGP(ip, auth, asnum, neighlist):
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/router/bgp={asnum}"
    data = {
        "Cisco-IOS-XE-bgp:bgp": {
            "id": asnum,
            "bgp": {
                "log-neighbor-changes": True
            },
            "neighbor": neighlist
        }
    }

    return lib.createConfig(url, auth, data)

def main():
    ip = "192.168.50.1"
    auth = ("hq-adm","hq-adm")

    neighbors = {
        "1" : {
            "ip" : "202.107.7.1",
            "asnum" : 65001
        }
    }

    nlist =[]

    for n in neighbors:
        nlist.append(addBGPNeighbor(neighbors[n]["ip"], neighbors[n]["asnum"]))
    
    print (configBGP(ip, auth, 65002, nlist))
    print (lib.saveConfig(auth, ip))
    
    

if __name__ == "__main__":
    main()
