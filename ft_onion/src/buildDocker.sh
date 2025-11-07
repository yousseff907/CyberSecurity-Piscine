#!/bin/bash
echo "Building docker image"
docker build -t ft_onion .
echo "Running container"
docker run -d --name ft_onion_container -p 2424:4242 ft_onion
echo "Wait 30 seconds for initialization"
sleep 30
echo "Creating your .onion adress"
docker exec ft_onion_container cat /var/lib/tor/hidden_service/hostname
echo "Container status"
docker ps
echo "Running services"
docker exec ft_onion_container ps aux | grep 'ssh|tor|nginx'
echo "For testing"
echo "SSH: ssh -i ~/.ssh/ft_onion -p 2424 root@localhost"
echo "Web: Open Tor Browser and visit the .onion address above"