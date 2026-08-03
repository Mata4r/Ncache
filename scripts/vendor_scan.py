
from scapy.all import Ether, ARP, srp
from scapy.utils import valid_mac
from mac_vendor_lookup import MacLookup
from rich.console import Console
import time

console = Console()

def vendor(Target,
           save=False):

    start = time.perf_counter()
    
    lookup = MacLookup()
    
    
    if valid_mac(Target):
        vendor = lookup.lookup(Target)
        
        console.print(f"Mac Address\t\tVendor", style="italic magenta")
        print(f"{Target}\t{vendor}")
    else:
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp = ARP(pdst=Target)
        
        answered, unanswered = srp(
            ether / arp,
            timeout=3,
            verbose=False
            )
        
        for sent, recv in answered:
            try:
                vendor = lookup.lookup(recv.hwsrc)
            except Exception:
                vendor = "Unknown"
            print()
        console.print(f"Mac Address\t\tVendor", style="magenta")
        result = print(f"{recv.hwsrc}\t{vendor}")

        elapsed = time.perf_counter() - start
        print(f"\nScan completed in {elapsed:.2f} seconds\n")
        
        
    if save:
        print()
        txt_save = input("FileName: ")
                
        with open(f"{txt_save}.txt", "w") as txt_file:
            txt_file.write(f"Mac Address\t\t    Vendor")
            txt_file.write(f"\n{recv.hwsrc}\t{vendor}")