
from scapy.all import sniff, IP, Ether, ICMP, sendp, ARP
from mac_vendor_lookup import MacLookup
from rich.console import Console

devices = {}
console = Console()

def packet_listener(packet,
                    Target):
    
    Target_split = Target.split(".")
    network_prefix = Target_split[0]      


    if IP in packet and Ether in packet:
        ip_address = packet[IP].src
        mac_address = packet[Ether].src   
    elif ARP in packet:
        ip_address = packet[ARP].psrc
        mac_address = packet[ARP].hwsrc
    else:
        return
        
        
    if not ip_address.startswith(network_prefix):
        return

    lookup = MacLookup()


    if ip_address not in devices:
        try:
            vendor = lookup.lookup(mac_address)
        except Exception:
            vendor = "Unknown"
                
        devices[ip_address] = (mac_address, vendor)
        print(f"{ip_address}\t{mac_address}   {vendor}")

def start_passive_scan(subnet, save=False):
    
    print("\nListening...")
    print("Press Ctrl+C to stop.\n")
  
    print(f"-Initiating Ncache scan\n-Ncache scan report for {Target}\n")
    console.print("IP address\tMac Address\t    Vendor", style="italic magenta")

    try:
        result = sniff(prn=lambda pkt: packet_listener(pkt, subnet), store=False)
    except KeyboardInterrupt as e:
        print(e)
    
    
    if save:
        print()
        txt_save = input("FileName: ")
        
        with open(f"{txt_save}.txt", "w") as txt_file:
            txt_file.write("IP Address\t    MAC Address\t        Vendor\n")
                
            for ip, (mac, vendor) in devices.items():
                txt_file.write(f"{ip}\t{mac}   {vendor}\n")
