from netmiko import ConnectHandler
from getpass import getpass
print("Input pass :")
passw = input()

ios_xe_routers = ["cisco3.lasthop.io", "cisco4.lasthop.io"]

for ip in ios_xe_routers:

    ios_xe_credentials = {"host": ip, "username": "pyclass", "password": passw, "device_type": "cisco_xe", "session_log": (f"{ip}.log")}
    net_connect = ConnectHandler(**ios_xe_credentials)
    print(f"we are connected to {net_connect.find_prompt()}")
    #print(net_connect.find_prompt())
    show_ver = net_connect.send_command("show ip int br")
    print(show_ver)

arista_routers = ["arista1.lasthop.io", "arista2.lasthop.io", "arista3.lasthop.io","arista4.lasthop.io"]
arista_credentials = {}

juniper_routers = []
juniper_credentials = {}


nexus_switches = []
nexus_credentials = {}
