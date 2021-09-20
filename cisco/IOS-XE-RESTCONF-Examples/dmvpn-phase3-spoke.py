import restconf_lib as lib

ip = "192.168.50.1"
url = "https://192.168.50.1/restconf/data/Cisco-IOS-XE-native:native/interface/Tunnel=1"
auth = ("hq-adm", "hq-adm")
data = {
  "Cisco-IOS-XE-interface:Tunnel": {
    "name": 1,
    "ip": {
      "address": {
        "primary": {
          "address": "10.0.0.2",
          "mask": "255.255.255.224"
        }
      },
      "Cisco-IOS-XE-nhrp:nhrp": {
        "authentication": "NHRP-KEY",
        "map": {
          "dest-ipv4": [
            {
              "dest-ipv4": "10.0.0.1",
              "nbma-ipv4": [
                {
                  "nbma-ipv4": "202.107.7.2"
                }
              ]
            }
          ],
          "multicast": {
            "nbma_ipv4": [
              "202.107.7.2"
            ]
          }
        },
        "network-id": 1,
        "nhs": {
          "ipv4": [
            {
              "ipv4": "10.0.0.1"
            }
          ]
        },
        "shortcut": {}
      },
      "Cisco-IOS-XE-ospf:ospf": {
          "network": "point-to-multipoint",
          "priority": 0
      }
    },
    "Cisco-IOS-XE-tunnel:tunnel": {
      "source": "GigabitEthernet3",
      "mode": {
        "gre": {
          "multipoint": {}
        }
      }
    }
  }
}

print (lib.createConfig(url, auth,data))
print (lib.saveConfig(auth, ip))
