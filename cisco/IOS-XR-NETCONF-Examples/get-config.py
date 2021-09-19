import netconf_library as lib

con = lib.Connect("172.16.10.1", 830, "isp-adm", "isp-adm", {"name" : "iosxr"})
filter = """
<filter>
<host-names xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-cfg" />
</filter>
"""
print (lib.getConfig(con, filter=filter))

