
from scapy.all import get_if_hwaddr, conf
from rich.console import Console
import socket

console = Console()

def system_info():
    
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(socket.gethostname())
        mac_address = get_if_hwaddr(conf.iface)

        console.print(f"hostname\tMac Address\t\tIp Address", style="italic magenta")
        print(f"{hostname}\t\t{mac_address}\t{local_ip}")
    except Exception as e:
        print(f"Error occurred: {e}")