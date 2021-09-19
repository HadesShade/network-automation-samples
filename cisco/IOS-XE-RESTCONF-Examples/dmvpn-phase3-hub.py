import restconf_lib as lib

ip = "172.16.10.20"
url = "https://172.16.10.20/restconf/data/Cisco-IOS-XE-native:native/interface/Tunnel=1"
auth = ("ro-adm","ro-adm")

data = {
  "Cisco-IOS-XE-native:Tunnel": {
    "name": 1,
    "ip": {
      "address": {
        "primary": {
          "address": "10.0.0.1",
          "mask": "255.255.255.224"
        }
      },
      "Cisco-IOS-XE-nhrp:nhrp-v4": {
        "nhrp": {
          "map": {
            "multicast": {
              "dynamic": [
                  None
              ]
            }
          },
          "authentication": "NHRP-KEY",
          "network-id": 1,
          "redirect": {}
        }
      },
      "Cisco-IOS-XE-ospf:router-ospf": {
        "ospf": {
          "network": {
            "point-to-multipoint": {}
          }
        }
      }
    },
    "Cisco-IOS-XE-tunnel:tunnel": {
      "source": "GigabitEthernet3",
      "mode": {
        "gre-config": {
          "multipoint": {}
        }
      }
    }
  }
}

print (lib.createConfig(url,auth,data))
print (lib.saveConfig(auth, ip))