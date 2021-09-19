import restconf_lib as lib

ip = "172.16.10.20"
url = "https://172.16.10.20/restconf/data/Cisco-IOS-XE-native:native/interface/Tunnel=1"
auth = ("ro-adm", "ro-adm")
data = {
  "Cisco-IOS-XE-native:Tunnel": {
    "name": 1,
    "ip": {
      "address": {
        "primary": {
          "address": "10.0.0.2",
          "mask": "255.255.255.224"
        }
      },
      "Cisco-IOS-XE-nhrp:nhrp-v4": {
        "nhrp": {
          "map": {
            "dest-ipv4": [
              {
                "dest-ipv4": "10.0.0.1",
                "nbma-ipv4": [
                  {
                    "nbma-ipv4": "200.100.50.6"
                  }
                ]
              }
            ],
            "multicast": {
              "nbma_ipv4": [
                "200.100.50.6"
              ]
            }
          },
          "nhs": {
            "ipv4": [
              {
                "ipv4": "10.0.0.1"
              }
            ]
          },
          "authentication": "NHRP-KEY",
          "network-id": 1,
          "shortcut": {}
        }
      },
      "Cisco-IOS-XE-ospf:router-ospf": {
        "ospf": {
          "network": {
            "point-to-multipoint": {}
          },
          "priority": 0
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

print (lib.createConfig(url, auth,data))
print (lib.saveConfig(auth, ip))
