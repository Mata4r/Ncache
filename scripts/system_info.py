
from scapy.all import get_if_hwaddr, conf
from rich.console import Console
from rich import print
import socket

console = Console()

def system_info():
    
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(socket.gethostname())
        mac_address = get_if_hwaddr(conf.iface)
        
        print(f"[magenta]Hostname:[/magenta]{hostname}")
        print(f"[magenta]Ip Address:[/magenta]{local_ip}")
        print(f"[magenta]Mac Address:[/magenta]{mac_address}")
    except Exception as e:
        print(f"Error occurred: {e}")
