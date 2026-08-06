
from scapy.all import IP, ICMP, srp, Ether, ARP
from rich.console import Console
from mac_vendor_lookup import MacLookup
import time

console = Console()

def start_host_scan(Target,
                    save=False):

    start = time.perf_counter()
    results = []

    try:
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp = ARP(pdst=Target)
        answered, unanswered = srp(
            ether / arp,
            timeout=3,
            verbose=False
        )
    except Exception as e:
        print(e)
        return

    lookup = MacLookup()
    
    if answered:
        print()
        print(f"-Initiating Ncache scan\n-Ncache scan report for {Target}\n")
        console.print("IP Address\tMAC Address\t\tVendor", style="italic magenta")
        seen = set()

        for sent, recv in answered:
            if recv.psrc in seen:
                continue
            seen.add(recv.psrc)
            try:
                vendor = lookup.lookup(recv.hwsrc)
            except Exception:
                vendor = "Unknown"

            print(f"{recv.psrc}\t{recv.hwsrc}\t{vendor}")
            results.append((recv.psrc, recv.hwsrc, vendor))
    else:
        print(f"No responsive {Target}")

    elapsed = time.perf_counter() - start
    print(f"\nScan completed in {elapsed:.2f} seconds\n")
    
    if save:
        print()
        txt_save = input("FileName: ")
        
        with open(f"{txt_save}.txt", "w") as txt_file:
            txt_file.write("IP Address\t    MAC Address\t       Vendor\n")
            for ip, mac, vendor in results:
                txt_file.write(f"{ip}\t{mac}\t{vendor}\n")
