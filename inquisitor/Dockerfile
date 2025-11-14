# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yitani <yitani@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/13 12:31:30 by yitani            #+#    #+#              #
#    Updated: 2025/11/13 23:29:58 by yitani           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
	net-tools \
	python3 \
	python3-pip \
	libpcap-dev \
	ftp \
	iputils-ping \
	tcpdump

RUN pip3 install scapy

CMD ["tail", "-f", "/dev/null"]