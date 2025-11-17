#!/bin/bash

echo "[*] Connecting to FTP server..."
echo "[*] Credentials: ftpuser / ftppass"
echo ""

docker exec -it victim ftp 192.168.1.100