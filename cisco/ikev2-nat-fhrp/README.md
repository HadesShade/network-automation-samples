IKEV2 with FHRP and NAT Cisco LAB using EVE-NG

Topology : 
![image](https://user-images.githubusercontent.com/54205634/127513869-9f5b949b-4c37-49de-8d6b-b62cd473a919.png)

Configuration List :

1. VRRP on Internal Network of R1 and R2 with Line-Protocol tracking to Outside Interface
2. HSRP on Outside Interface of R1 and R2 with name "INET-FHRP" and Line-Protocol tracking to Inside Interface
3. IKEV2 IPSEC L2L Between ASA, R1 Router, and R2 Router. 
4. Crypto map that used in R1 and R2 routers are configured with "INET-FHRP" redudancy.
5. NAT/PAT exemption on R1, R2, and ASA (The "interesing traffic" defined for IKEV2 IPSEC is excluded from the NAT roles)
6. BGP Routing.
7. DHCP on Internal Network of R1 and R2.
8. Embedded Event Manager (EEM) Script that will executed when the failover occur between R1 and R2 routers. 
   The script will refresh the status of IKEV2 SA on routers.
   
Note : The switches used in this topology are in "no configuration" state. 

Configuration for ASA : ASA.cfg
Configuration for R1 and R2 routers : R1.cfg and R2.cfg
