#!/bin/bash

echo "[*] Getting MAC addresses..."
VICTIM_MAC=$(docker exec victim cat /sys/class/net/eth0/address)
FTP_MAC=$(docker exec ftp_server cat /sys/class/net/eth0/address)

echo "[*] Victim MAC: $VICTIM_MAC"
echo "[*] FTP Server MAC: $FTP_MAC"
echo "[*] Starting ARP poisoning attack..."
echo ""

docker exec -it attacker python3 /app/inquisitor.py 192.168.1.10 $VICTIM_MAC 192.168.1.100 $FTP_MAC