import restconf_lib as lib

def addACLSequence(seqNum, action, ipv4_prefix, wildcard_mask):
    data_permit = {
        "sequence": seqNum,
        "permit": {
          "std-ace": {
            "ipv4-prefix": ipv4_prefix,
            "mask": wildcard_mask
          }
        }
    }

    data_deny = {
        "sequence": seqNum,
        "deny": {
          "std-ace": {
            "ipv4-prefix": ipv4_prefix,
            "mask": wildcard_mask
          }
        }
    }

    if action == "permit":
        return data_permit
    elif action == "deny":
        return data_deny
    else:
        return "Error! Action should be either 'permit' or 'deny'."

def configStandardACL(ip, auth, name, seq_rule):
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/standard={name}"
    data = {
        "Cisco-IOS-XE-acl:standard": {
            "name": name,
            "access-list-seq-rule": seq_rule
        }
    }

    return lib.createConfig(url, auth, data)
  
def main():
  ip = "192.168.50.1"
  auth = ("hq-adm","hq-adm")

  seqlist = {
    10 : {
      "net" : "192.168.10.0",
      "wildcard" : "0.0.0.255",
      "act" : "permit"
    },

    20 : {
      "net" : "192.168.50.0",
      "wildcard" : "0.0.0.255",
      "act" : "permit"
    }
  }

  seqrules = []

  for s in seqlist:
    seqrules.append(addACLSequence(s, seqlist[s]["act"], seqlist[s]["net"], seqlist[s]["wildcard"]))
  
  print (configStandardACL(ip, auth, "NAT", seqrules))
  print (lib.saveConfig(auth, ip))

if __name__ == "__main__":
  main()