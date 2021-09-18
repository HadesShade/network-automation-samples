import netconf_library as lib

con = lib.Connect("172.16.10.1", 830, "isp-adm", "isp-adm", {"name" : "iosxr"})
filter = """
<filter>
<bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-bgp-cfg" />
</filter>
"""
print (lib.getConfig(con, filter=filter))

