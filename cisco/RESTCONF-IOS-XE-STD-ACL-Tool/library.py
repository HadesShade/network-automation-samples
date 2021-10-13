import requests, json
from ipaddress import IPv4Address
requests.packages.urllib3.disable_warnings()

head = {
	"Accept" : "application/yang-data+json",
	"Content-Type" : "application/yang-data+json"
}

auth = ("admin", "Passw0rd$")

def saveConfig(ip):
	url = f"https://{ip}/restconf/operations/cisco-ia:save-config"
	res = requests.post(url, auth=auth, headers=head, verify=False)
	return f"Status : {res.status_code}" if res.status_code in range(200,300) else f"Status : {res.content}"

def constructURL1(ip):
	return f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/standard"

def constructURL2(ip):
	return f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/interface"

def operateACL(url, op, name, net=" ", pfx=" ", act=" ", seqNum = " "):
	if op == "create":
		if net != " ":
			wild = str(IPv4Address(int(IPv4Address._make_netmask(pfx)[0])^(2**32-1)))
			data = {
 				 "Cisco-IOS-XE-acl:standard": [
    					{
      						"name": name,
      						"access-list-seq-rule": [
        					{
          						"sequence": seqNum,
          					       	 act : {
            							"std-ace": {
              								"ipv4-prefix": net,
              								"mask": wild
            							}
          						}
        					}
      						]
    					}
  				]
			}

			res = requests.patch(url, data=json.dumps(data), auth=auth, headers=head, verify=False)

		else:
			data = {
				"Cisco-IOS-XE-acl:standard":
				{
					"name" : name
				}
			}
			res = requests.patch(url, data=json.dumps(data), auth=auth, headers=head, verify=False)

		return f"Status : {res.status_code}" if res.status_code in range(200,300) else f"Status : {res.content}"

	else:
		if net != " ":
			wild = str(IPv4Address(int(IPv4Address._make_netmask(pfx)[0])^(2**32-1)))
			res = requests.delete(url + f"={name}/access-list-seq-rule={seqNum}", auth=auth, headers=head, verify=False)

		else:
			res = requests.delete(url + f"={name}", auth=auth, headers=head, verify=False)


def listACL(url):
	res = requests.get(url, headers=head, auth=auth, verify=False)
	return json.dumps(res.json(), indent=2) if res.status_code in range(200,300) else res.content

def applyACL(url, act, name, gress, int):
	newURL = url + f"/{int}/ip/access-group"
	if act == "enable":
		data = {
			"Cisco-IOS-XE-native:access-group": {
    				gress: {
      					"acl": {
        					"acl-name": name,
        					gress: [ None ]
      					}
    				}
			}
		}

		res = requests.patch(newURL, data=json.dumps(data), headers=head, auth=auth, verify=False)

	else:
		data = {
			"Cisco-IOS-XE-native:access-group": {
    				gress: {
      					"acl": {
        					"acl-name": name,
        					gress: [ None ]
      					}
    				}
			}
		}

		res = requests.delete(newURL, data=json.dumps(data), headers=head, auth=auth, verify=False)

	return f"Status : {res.status_code}" if res.status_code in range(200,300) else f"Status : {res.content}"
