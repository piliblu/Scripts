#!/usr/bin/env python3
import scapy.all as scapy

packetARP = scapy.ARP(op="2", pdst="10.0.2.3" , hwdst="52:54:00:12:35:02", psrc="10.0.2.2")
print(packetARP.summary())
