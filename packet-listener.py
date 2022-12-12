'''
Developed by ErWin

E-22 NWL is a basic Packet Listener built with Python

'''

import http
import scapy.all as scapy
import time
import os
from scapy.layers.http import *

def listen_packets(interface):
  scapy.sniff(iface = interface , store = False , prn = analyze_packets)



def analyze_packets(packet):
  if packet.haslayer(http.HTTPRequest):
    if packet.haslayer(scapy.Raw):
      print(packet[scapy.Raw].load)

listen_packets("eth0")
