import netconf_library as lib

hostname = {
    "HOSTNAME" : "ISP4"
}

con = lib.Connect("172.16.10.1", 830, "isp-adm", "isp-adm", {"name" : "iosxr"})

final = lib.GenerateConfig(hostname, "hostname.xml")
lib.editConfig(con, final)