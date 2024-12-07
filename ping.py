#!/usr/bin/env python
for i in range (1,5):
    print(f'ping 192.168.1.{i}')
net_base = "192.168.1."
for n in range(1,6):
    print(f"ping {net_base}{n}")

with open("ospf.cfg", 'w') as f:
    for ospf_id in range(1,3):
        f.write(f"router ospf {ospf_id}\n")
        f.write(f"network {net_base}{n}\n")    
