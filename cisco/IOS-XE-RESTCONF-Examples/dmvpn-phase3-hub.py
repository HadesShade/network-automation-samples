import restconf_lib as lib

ip = "192.168.50.1"
url = "https://192.168.50.1/restconf/data/Cisco-IOS-XE-native:native/interface/Tunnel=1"
auth = ("hq-adm","hq-adm")

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
      "Cisco-IOS-XE-nhrp:nhrp": {
        "authentication": "NHRP-KEY",
        "map": {
          "multicast": {
            "dynamic": [
              None
            ]
          }
        },
        "network-id": 1,
        "redirect": {}
      },
      "Cisco-IOS-XE-ospf:ospf": {
          "network": "point-to-multipoint"
      }
    },
    "Cisco-IOS-XE-tunnel:tunnel": {
      "source": "GigabitEthernet1",
      "mode": {
        "gre": {
          "multipoint": {}
        }
      }
    }
  }
}

print (lib.createConfig(url,auth,data))
print (lib.saveConfig(auth, ip))