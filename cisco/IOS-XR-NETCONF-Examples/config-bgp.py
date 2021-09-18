import netconf_library as lib

con = lib.Connect("172.16.10.1", 830, "isp-adm", "isp-adm", { "name" : "iosxr"})

network = {
    "1" : {
        "NET_ADDR" : "4.4.4.4",
        "NET_PREFIX" : "32"
    },

    "2" : {
        "NET_ADDR" : "172.16.10.0",
        "NET_PREFIX" : "24"
    }
}

neigbor = {
    "1" : {
        "NEIGH_ADDR" : "200.100.50.2",
        "AS_XX" : "0",
        "AS_YY" : "65001"
    },

    "2" : {
        "NEIGH_ADDR" : "200.100.50.6",
        "AS_XX" : "0",
        "AS_YY" : "65003"
    }
}

configNet = ""
for c in network:
    configNet += lib.GenerateConfig(network[c], "bgp-network.xml")

configNeigh = ""
for i in neigbor:
    configNeigh += lib.GenerateConfig(neigbor[i], "bgp-neighbor.xml")

bgp = {
    "INS_NAME" : "default",
    "INS_AS" : "0",
    "FB_AS" : "65004",
    "AF_NAME" : "ipv4-unicast",
    "NET_LIST" : configNet,
    "NEIGH_LIST" : configNeigh
}

final = lib.GenerateConfig(bgp, "bgp-template.xml")
# print (final)
lib.editConfig(con, final)


