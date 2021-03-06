import netconf_library as lib

interfaces = {
    "1" : {
        "IFNAME" : "GigabitEthernet0/0/0/1",
        "DESCRIPTION" : "TO-HQ",
        "IPV4_ADDR" : "202.107.7.1",
        "MASK" : "255.255.255.252",
        "ISVIRTUAL" : "",
        "ISSHUTDOWN" : '<shutdown xc:operation="delete" />'
    },

    "2" : {
        "IFNAME" : "GigabitEthernet0/0/0/2",
        "DESCRIPTION" : "TO-BR1",
        "IPV4_ADDR" : "202.107.7.5",
        "MASK" : "255.255.255.252",
        "ISVIRTUAL" : "",
        "ISSHUTDOWN" : '<shutdown xc:operation="delete" />'
    },

    "3" : {
        "IFNAME" : "GigabitEthernet0/0/0/3",
        "DESCRIPTION" : "TO-BR2",
        "IPV4_ADDR" : "202.107.7.9",
        "MASK" : "255.255.255.252",
        "ISVIRTUAL" : "",
        "ISSHUTDOWN" : '<shutdown xc:operation="delete" />'
    },

    "4" : {
        "IFNAME" : "Loopback1111",
        "DESCRIPTION" : "LOOPBACK",
        "IPV4_ADDR" : "1.1.1.1",
        "MASK" : "255.255.255.255",
        "ISVIRTUAL" : "<interface-virtual />",
        "ISSHUTDOWN" : ""
    }
}

intConfig = ""

for i in interfaces:
    intConfig += lib.GenerateConfig(interfaces[i], "interface-iterator.xml")

final = lib.GenerateConfig({"INTERFACE_LIST" : intConfig}, "interface-template.xml")
# print (final)
con = lib.Connect("172.16.10.1", 830, "isp-adm", "isp-adm", {"name" : "iosxr"})
lib.editConfig(con, final)