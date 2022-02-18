#!/usr/bin/env python3
import subprocess
import optparse
import re

def mactwister(interface, mac):
    print("[+] Changing MAC address for interface " + options.interface + " to " + options.mac)
    subprocess.call(["ifconfig ", interface, " down"])
    subprocess.call(["ifconfig ", interface, "hw ",  "ether ", mac])
    subprocess.call(["ifconfig ", interface, " up"]) 
def getoptions()
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface: #code to handle error
        parser.error("[+] Please specify an interface, use --help for more info")
    elif not options.mac: #error handle error
        parser.error("[+] Please specify a MAC, use --help for more info")
    return options


options = getoptions()
# mactwister(options.interface, options.mac)

ifconfig = subprocess.check_output(["ifconfig", options.interface])

macaddressresult = re.search(r"\w\w:\w\w:\w\w:\w\w:", ifconfig)
print
