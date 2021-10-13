#!/usr/bin/python3

import library as lib
import argparse

def main():
	arg = argparse.ArgumentParser(description="Operate ACLs with RESTCONF", allow_abbrev=False)
	arg.add_argument ('--router', action='store', type=str, required=True)
	arg.add_argument ('--create-acl', action='store', type=str)
	arg.add_argument ('--delete-acl', action='store', type=str)
	arg.add_argument ('--create-rule', action='store_true')
	arg.add_argument ('--delete-rule', action='store_true')
	arg.add_argument ('--acl', action='store', type=str)
	arg.add_argument ('--ingress', action='store_true')
	arg.add_argument ('--egress', action='store_true')
	arg.add_argument ('--allow', action='store', type=str)
	arg.add_argument ('--deny', action='store', type=str)
	arg.add_argument ('--prio', action='store', type=int)
	arg.add_argument ('--apply-acl', action='store_true')
	arg.add_argument ('--disable-acl', action='store_true')
	arg.add_argument ('--interface', action='store', type=str, help="Use Full name with = for separator between numbers. Ex : GigabitEthernet=2")
	arg.add_argument ('--list', action='store_true')

	args = arg.parse_args()

	url1 = lib.constructURL1(args.router)
	url2 = lib.constructURL2(args.router)


	if args.create_acl:
		a = lib.operateACL(url1, "create", args.create_acl)
		print (a)

	elif args.delete_acl:
		a = lib.operateACL(url1, "delete", args.delete_acl)
		print (a)

	elif args.create_rule:
		n = args.allow.split('/') if args.allow else args.deny.split('/')
		net = n[0]
		pfx = n[1]
		a = lib.operateACL(url1, "create", args.acl, net, pfx, act="permit" if args.allow else "deny", seqNum=args.prio)
		print (a)

	elif args.delete_rule:
		n = args.allow.split('/') if args.allow else args.deny.split('/')
		net = n[0]
		pfx = n[1]
		a = lib.operateACL(url1, "delete", args.acl, net, pfx, act="permit" if args.allow else "deny", seqNum=args.prio)
		print (a)

	elif args.list:
		a = lib.listACL(url1)
		print (a)

	elif args.apply_acl:
		if args.ingress:
			traf = "in"
		elif args.egress:
			traff = "out"
		else:
			print ("Please Define --ingress or --egress")
			exit()
		a = lib.applyACL(url2, "enable", args.acl, traf, args.interface)
		print (a)

	elif args.disable_acl:
		if args.ingress:
			traf = "in"
		elif args.egress:
			traff = "out"
		else:
			print ("Please Define --ingress or --egress")
			exit()
		a = lib.applyACL(url2, "disable", args.acl, traf, args.interface)
		print (a)

	else:
		print ("Broken Options!")

	print (lib.saveConfig(args.router))

if __name__ == "__main__":
	main()
