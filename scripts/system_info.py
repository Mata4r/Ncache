
from scapy.all import get_if_hwaddr, conf
from rich.console import Console
import socket

console = Console()

def system_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(socket.gethostname())
        mac_address = get_if_hwaddr(conf.iface)
        
        print(f"Hostname:{hostname}")
        print(f"Ip Address:{local_ip}")
        print(f"Mac Address:{mac_address}")
    except Exception as e:
        print(f"Error occurred: {e}")
