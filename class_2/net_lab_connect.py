from netmiko import ConnectHandler, file_transfer
from getpass import getpass
from pprint import pprint
print("Input pass :")
passw = input()

ios_xe_routers = ["cisco3.lasthop.io"]
#ios_xe_routers = ["cisco3.lasthop.io", "cisco4.lasthop.io"]

arista_routers = ["arista1.lasthop.io", "arista2.lasthop.io", "arista3.lasthop.io","arista4.lasthop.io"]

for ip in ios_xe_routers:

    ios_xe_credentials = {
        "host": ip,
        "username": "pyclass",
        "password": passw,
        "device_type": "cisco_xe",
        "use_keys" : False,
        "key_file": "/home/user/.ssh/test.rsa",
        "session_log": (f"{ip}.log")}

    net_connect = ConnectHandler(**ios_xe_credentials)
    print(f"we are connected to {net_connect.find_prompt()}")
    #print(net_connect.find_prompt())
    show_ver = net_connect.send_command("show ip int br", delay_factor=5,use_textfsm=True)
    # .send_config_set(list_of_cmd)
    # .send_config_from_file(config_file='config.txt')'
    #net_connect.save_config()
    # net_connect.send_command('commit confirmed 5')
    
pprint(show_ver)
    for intf in show_ver:
        ip = (intf['ip_address'])
        intf_name = intf['interface']
        if ip != 'unassigned':
            print(f'this is interface {intf_name} ip {ip}')
"""
    cmd_delete = "delete flash:/cisco_file.txt"
    del_file = net_connect.send_command(cmd_delete, expect_string=r"\[cisco_file.txt\]\?")
    del_file += net_connect.send_command("y", expect_string=r"\[confirm\]")
    del_file += net_connect.send_command("\n")
    print(del_file)
"""
