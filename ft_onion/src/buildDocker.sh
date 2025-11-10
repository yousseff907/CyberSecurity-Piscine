#!/bin/bash
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    buildDocker.sh                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yitani <yitani@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/10 15:39:55 by yitani            #+#    #+#              #
#    Updated: 2025/11/10 15:40:02 by yitani           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

docker build -t ft_onion .
echo "Running container"
docker run -d --name ft_onion_container -p 2424:4242 ft_onion
echo "Creating your .onion adress"
docker exec ft_onion_container cat /var/lib/tor/hidden_service/hostname
echo "Container status"
docker ps
echo "Running services"
docker exec ft_onion_container ps aux | grep 'ssh|tor|nginx'
echo "For testing"
echo "SSH: ssh -i ~/.ssh/ft_onion -p 2424 root@localhost"
echo "Web: Open Tor Browser and visit the .onion address above"