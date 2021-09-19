from jinja2 import Template
from ncclient import manager

def Connect(host, port, username, password, device_params):
    return manager.connect(host=host, port=port, username=username, password=password, device_params=device_params, hostkey_verify=False)

def GetCapabilities(Connection):
    for c in Connection.server_capabilities:
        print (c)

def getConfig(Connection, filter=""):
    return Connection.get_config(source="running") if filter == "" else Connection.get_config(source="running", filter=filter)

def editConfig(Connection, configData):
    operation = Connection.edit_config(target="candidate", config=configData)
    print ("Operation Result : ")
    print (operation)
    commit = Connection.commit()
    print ("Commit Result : ")
    print (commit)

def GenerateConfig (data, file):
    tempFile = open(file,"r")
    temp = Template(tempFile.read())
    return temp.render(data)
