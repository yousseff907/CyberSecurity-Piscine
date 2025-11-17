# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yitani <yitani@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/13 12:31:30 by yitani            #+#    #+#              #
#    Updated: 2025/11/17 11:35:12 by yitani           ###   ########.fr        #
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
	tcpdump \
	&& rm -rf /var/lib/apt/lists/*

RUN pip3 install scapy netifaces

WORKDIR /app
COPY src/ /app/

CMD ["tail", "-f", "/dev/null"]