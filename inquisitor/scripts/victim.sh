#!/bin/bash
echo "
docker exec -it victim ftp
open 192.168.1.100 21
ftpuser
ftppass
ls
get ftp.txt
put /etc/hostname uploaded.txt
bye
EOF

echo ""
echo "[*] FTP session completed"
"