from netmiko import ConnectHandler
from getpass import getpass


def connect_to_device(device_type, ip, username, password):
    """Connects to a device using Netmiko."""
    credentials = {
        "host": ip,
        "username": username,
        "password": password,
        "device_type": device_type,
        "session_log": (f"{ip}.log"),
        "verbose": True
    }
    try:
        net_connect = ConnectHandler(**credentials)
        return net_connect
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")
        return None

def get_cmd_result(net_connect, ip):
    """Gets the version of a device."""
    try:
        show_ver = net_connect.send_command("show version")
     
        with open((f'show_ver.{ip}.txt'),'w') as f:
            f.write(show_ver)
        print(f"Version info written to file for {ip}")
    except Exception as e:
        print(f"Failed to get version from {ip}: {e}")


""" Main Function Body """


def main():
    banner = "#"*50
    password = getpass("Input password for TACACS: ")
    username = "pyclass"

    ios_xe_routers = ["cisco3.lasthop.io", "cisco4.lasthop.io"]
    nxos_switches = ["nxos1.lasthop.io", "nxos2.lasthop.io"]

    for ip in ios_xe_routers:
        net_connect = connect_to_device("cisco_xe", ip, username, password)
        if net_connect:
            hostname = str(net_connect.find_prompt()).split('#')[0]
            print(f"Connected to {hostname}")
            show_ip_int_br = net_connect.send_command("show ip int br")
            ext_ping = net_connect.send_command_timing("ping", strip_prompt=False, strip_command=False)
            ext_ping += net_connect.send_command_timing("ip", strip_prompt=False, strip_command=False)
            ext_ping += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
            ext_ping += net_connect.send_command_timing("3", strip_prompt=False, strip_command=False) 
            ext_ping += net_connect.send_command_timing("200", strip_prompt=False, strip_command=False) 
            ext_ping += net_connect.send_command_timing("1", strip_prompt=False, strip_command=False)
            ext_ping += net_connect.send_command_timing("n", strip_prompt=False, strip_command=False)
            ext_ping += net_connect.send_command_timing("n") 
            
            
            print(show_ip_int_br)
            print(ext_ping)
            print(banner)
            get_cmd_result(net_connect, ip)
            print(f"Disconnecting from {ip}")
            print(banner)



if __name__ == "__main__":
    main()
            
	
	
	
