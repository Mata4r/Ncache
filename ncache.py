#!/usr/bin/env python3

import argparse

from scripts.arp_scan import start_arp_scan
from scripts.passive_scan import start_passive_scan
from scripts.icmp_scan import start_icmp_scan
from scripts.system_info import system_info
from scripts.vendor_scan import vendor
from scripts.host_scan import start_host_scan


def main():

    parser = argparse.ArgumentParser(description="Ncatch Network Scanner")

    parser.add_argument("-As", action="store_true", help="Scans Using ARP")
    parser.add_argument("-Ps", action="store_true", help="Scans Passively")
    parser.add_argument("-P", action="store_true", help="Scans Ports")
    parser.add_argument("-Is", action="store_true", help="Scans using ICMP")
    parser.add_argument("-Hs", action="store_true", help="Scans per IP")

    parser.add_argument("-T00", action="store_true", help="~1 Hour for a default /24 scan")
    parser.add_argument("-T0", action="store_true", help="~20 Min for a default /24 scan")
    parser.add_argument("-T1", action="store_true", help="~10 Min for a default /24 scan")
    parser.add_argument("-T2", action="store_true", help="~5 Min for a default /24 scan")
    parser.add_argument("-T3", action="store_true", help="~25 Sec for a default /24 scan")
    parser.add_argument("-T4", action="store_true", help="~5 Sec for a default /24 scan")

    parser.add_argument("-V", dest="Mac", help="Get vendor")
    parser.add_argument("-info", action="store_true", help="Get System info")

    parser.add_argument("-save", action="store_true", help="Save results")

    parser.add_argument("Target", nargs="?", help="Input Target")

    args = parser.parse_args()
    

    try:
        if args.As:
            if not args.Target:
                raise ValueError("Subnet is required for ARP scan")

            start_arp_scan(
                args.Target,
                args.save,
                args.T00,
                args.T0,
                args.T1,
                args.T2,
                args.T3,
                args.T4
            )


        elif args.Ps:
            if not args.Target:
                raise ValueError("Subnet is required for passive scan")

            start_passive_scan(
                args.Target,
                args.save
            )


        elif args.Is:
            if not args.Target:
                raise ValueError("Subnet is required for ICMP scan")

            start_icmp_scan(
                args.Target,
                args.save,
                args.T00,
                args.T0,
                args.T1,
                args.T2,
                args.T3,
                args.T4
            )


        elif args.Hs:
            if not args.Target:
                raise ValueError("Ip Address is required for host scan")

            start_host_scan(
                args.Target,
                args.save
            )

        elif args.info:
            system_info()


        elif args.Mac:
            if not args.Mac:
                raise ValueError("Mac Address is required from Vendor lookup")
            vendor(
                args.Mac,
                args.save
            )

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
