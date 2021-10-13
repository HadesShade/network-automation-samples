import requests, json

head = {
		"Content-Type" : "application/yang-data+json",
		"Accept" : "application/yang-data+json"
}

auth = ("admin","Passw0rd$")

res = requests.get("https://10.99.99.201/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/access-group", headers=head, auth=auth, verify=False)

print (json.dumps(res.json(), indent=2))
