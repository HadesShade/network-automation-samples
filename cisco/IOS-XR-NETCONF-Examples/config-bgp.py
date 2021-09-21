import netconf_library as lib

con = lib.Connect("172.16.10.1", 830, "isp-adm", "isp-adm", { "name" : "iosxr"})

network = {
    "1" : {
        "NET_ADDR" : "1.1.1.1",
        "NET_PREFIX" : "32"
    },

    "2" : {
        "NET_ADDR" : "172.16.10.0",
        "NET_PREFIX" : "24"
    },

    "3" : {
        "NET_ADDR" : "202.107.7.0",
        "NET_PREFIX" : "30"
    },

    "4" : {
        "NET_ADDR" : "202.107.7.4",
        "NET_PREFIX" : "30"
    },

    "5" : {
        "NET_ADDR" : "202.107.7.8",
        "NET_PREFIX" : "30"
    }
}

afs = {
    "AF_NAME" : "ipv4-unicast",
    "POL_NAME_IN" : "bgp-allow",
    "POL_NAME_OUT" : "bgp-allow"
}

configAFS = lib.GenerateConfig(afs, "bgp-neighbor-afs.xml")

neigbor = {
    "1" : {
        "NEIGH_ADDR" : "202.107.7.2",
        "AS_XX" : "0",
        "AS_YY" : "65002",
        "NEIGH_AFS" : configAFS
    },

    "2" : {
        "NEIGH_ADDR" : "202.107.7.6",
        "AS_XX" : "0",
        "AS_YY" : "65003",
        "NEIGH_AFS" : configAFS
    },

    "3" : {
        "NEIGH_ADDR" : "202.107.7.10",
        "AS_XX" : "0",
        "AS_YY" : "65004",
        "NEIGH_AFS" : configAFS
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
    "FB_AS" : "65001",
    "AF_NAME" : "ipv4-unicast",
    "NET_LIST" : configNet,
    "NEIGH_LIST" : configNeigh
}

final = lib.GenerateConfig(bgp, "bgp-template.xml")
# print (final)
lib.editConfig(con, final)


