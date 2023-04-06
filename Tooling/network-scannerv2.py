#!/usr/bin/env python3
import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP range")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP range, use --help for more info.")
    return options

def scan(ip):
    arp = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = broadcast/arp
    good = scapy.srp(request, timeout=1, verbose=False)[0]

    good_list = []
    for i in good:
        good_dic = {"IP":i[1].psrc, "MAC":i[1].hwsrc}
        good_list.append(good_dic)
    return good_list

def results(results):
    print("IP\t\t\t\tMAC Address\n----------------------------------------------------------------------------")
    for i in results:
        print(i["IP"] + "\t\t\t" + i["MAC"])
options = get_arguments()
scan_result = scan(options.target)  
results(scan_result)
