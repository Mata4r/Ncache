
from scapy.all import sniff, IP, Ether, ICMP, sendp, sr
from rich.console import Console
import time

console = Console()

def start_icmp_scan(Target,
                    save=False,
                    T00=False,
                    T0=False,
                    T1=False,
                    T2=False,
                    T3=False,
                    T4=False):
    
    start = time.perf_counter()
    
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
            ip_layer = IP(dst=Target)
            icmp = ICMP()
            answered, unanswered = sr(
                ip_layer/icmp,
                inter=scan_time,
                timeout=5,
                verbose=False
            )
        except Exception as e:
            print(f"Error occurred: {e}")
            return
    
    seen = set()
    
    
    if answered:
        print()
        print(f"-Initiating Ncache scan\n-Ncache scan report for {Target}\n")
        console.print("IP Address",style="italic magenta")
        
        for sent, received in answered:
            ip_address = received[IP].src
            
            if ip_address not in seen:
                seen.add(ip_address)
                print(f"{ip_address}")
    else:
        print()
        
    elapsed = time.perf_counter() - start
    print(f"\nScan completed in {elapsed:.2f} seconds\n")
    
    
    if save:
        print()
        txt_save = input("FileName: ")
        
        results = list(seen)
            
        with open(f"{txt_save}.txt", "w") as txt_file:
            txt_file.write("IP Address\n")
                
            for ip in results:
                txt_file.write(f"{ip}\n")
