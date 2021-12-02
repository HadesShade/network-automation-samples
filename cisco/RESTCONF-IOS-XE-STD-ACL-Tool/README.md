IMPORTANT !!!

This tool is using RESTCONF with YANG data structure (no raw commands execution).
So the interface name declared should be :

1. Using full name of the interface.
   example : Instead of using 'g' for GigabitEthernet, use the full name "GigabitEthernet"

2. Number of the interface separated by '=' with the interface name.
   example : Instead of using 'g1' or 'GigabitEthernet1', use 'GigabitEthernet=1'.

Example usage of interface parameter:

./main.py --router 1.1.1.1 --apply-acl --acl DMZ --ingress --intterface GigabitEthernet=1
<br>./main.py --router 1.1.1.1 --disable-acl --acl DMZ --egress --intterface GigabitEthernet=1

Above rules should be obeyed so this tool will work as intended.

Full example of usage :

1. Creating Standard ACL with name "DMZ" to router 1.1.1.1 :
./main.py --router 1.1.1.1 --create-acl DMZ

2. Deleting Standard ACL with name "DMZ" in router 1.1.1.1 :
./main.py --router 1.1.1.1 --delete-acl DMZ

3. Creating Standard ACL with name "DMZ" to router 1.1.1.1 with specific rules (update existing or create the new one) :
./main.py --router 1.1.1.1 --create-rule --acl DMZ --allow 10.10.10/32 --prio 10

4. Delete specific rules of standard ACL with name "DMZ" in router 1.1.1.1 :
./main.py --router 1.1.1.1 --delete-rule --acl DMZ --allow 10.10.10/32 --prio 10

5. List all standard ACL in router 1.1.1.1 (in JSON format):
./main.py --router 1.1.1.1 --list

6. Enable standard ACL "DMZ" in interface GigabitEthernet2 in router 1.1.1.1 (incoming traffic) :
./main.py --router 1.1.1.1 --apply-acl --acl DMZ --ingress --interface GigabitEthernet=2

7. Disable standard ACL "DMZ" in interface GigabitEthernet2 in router 1.1.1.1 (outgoing traffic) :
./main.py --router 1.1.1.1 --apply-acl --acl DMZ --egress --interface GigabitEthernet=2









