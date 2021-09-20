import netconf_library as lib

con = lib.Connect("172.16.10.1", 830, "isp-adm", "isp-adm", {'name' : 'iosxr'})

policies = {
    "POL_NAME" : "bgp-allow",
    "RPL" : "route-policy bgp-allow",
    "POL" : "pass"
}

final = lib.GenerateConfig(policies, "routing-policy.xml")
lib.editConfig(con, final)