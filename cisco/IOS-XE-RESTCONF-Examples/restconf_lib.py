import json, requests

header1 = {
    "Content-Type" : "application/yang-data+json",
    "Accept" : "application/yang-data+json"
}

header2 = {
    "Accept" : "application/yang-data+json"
}

def getConfig(url, auth):
    requests.packages.urllib3.disable_warnings()
    return json.dumps(requests.get(url, auth=auth, headers=header2, verify=False).json(), indent=2)

def setConfig(url, auth, data):
    requests.packages.urllib3.disable_warnings()
    jsondata = json.dumps(data)
    res = requests.patch(url, auth=auth, headers=header1, data=jsondata, verify=False)
    return f"Result : {res.status_code}" if res.status_code in range(200,300) else f"Result : {res.content}"

def createConfig(url, auth, data):
    requests.packages.urllib3.disable_warnings()
    jsondata = json.dumps(data)
    res = requests.put(url, auth=auth, headers=header1, data=jsondata, verify=False)
    return f"Result : {res.status_code}" if res.status_code in range(200,300) else f"Result : {res.content}"

def deleteConfig(url, auth):
    requests.packages.urllib3.disable_warnings()
    res = requests.delete(url, auth=auth, headers=header2, verify=False)
    return f"Result : {res.status_code}" if res.status_code in range(200,300) else f"Result : {res.content}"

def saveConfig(auth, xeip):
    url = f"https://{xeip}/restconf/operations/cisco-ia:save-config"
    res = requests.post(url, auth=auth, headers=header1, verify=False)
    return f"Result : {res.status_code}" if res.status_code in range(200,300) else f"Result : {res.content}"