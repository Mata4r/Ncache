
from scapy.all import Ether, ARP, srp 
from mac_vendor_lookup import MacLookup
from rich.console import Console
import time

console = Console()

def start_arp_scan(Target,
                  save=False,
                  T00=False,
                  T0=False,
                  T1=False,
                  T2=False,
                  T3=False,
                  T4=False):
    
    start = time.perf_counter()
    results = []
    scan_time = None


    if T00:
        scan_time = 14.2
    elif T0:
        scan_time = 4.7
    elif T1:
        scan_time = 2.4
    elif T2:
        scan_time = 1.2
    elif T3:
        scan_time = 0.1
    elif T4:
        scan_time = 0
    else:
        scan_time = 0

    if scan_time is not None:
        try:
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp = ARP(pdst=Target)
            answered, unanswered = srp(ether/arp,
                                       timeout=7,
                                       verbose=False,
                                       inter=scan_time)
        except Exception as e:
            print(f"Error occurred: {e}")
            return
            
        lookup = MacLookup()
        seen = set()

        print(f"-Initiating Ncache scan\n-Ncache scan report for {Target}\n")
        console.print("IP Address\tMAC Address\t    Vendor",style="italic magenta")
        
        for sent, recv in answered:
            if recv.psrc in seen:
                continue
            seen.add(recv.psrc)
            try:
                vendor = lookup.lookup(recv.hwsrc)
            except Exception:
                vendor = "Unknown"

            print(f"{recv.psrc}\t{recv.hwsrc}   {vendor}")
            results.append((recv.psrc, recv.hwsrc, vendor))
                
    elapsed = time.perf_counter() - start
    
    print(f"\nScan completed in {elapsed:.2f} seconds")
    
    
    if save:
        print()
        txt_save = input("FileName: ")
    
        with open(f"{txt_save}.txt", "w") as txt_file:
            txt_file.write("IP Address\t\t    MAC Address\t        Vendor\n")
                
            for ip, mac, vendorr in results:
                txt_file.write(f"{ip}\t\t{mac}   {vendorr}\n")
