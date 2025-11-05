# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yitani <yitani@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/05 09:41:01 by yitani            #+#    #+#              #
#    Updated: 2025/11/05 10:04:31 by yitani           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import getpass
import argparse

def	validateFile(pathToFile):
	try:
		f = open(pathToFile)
		content = f.read()
		f.close()
		content = content.strip()
	except Exception:
		print("Error was encountered opening file")
		exit(1)
	if len(content) < 64:
		print("More than 64 values found")
		exit(1)
	for c in content:
		if not c in ("0123456789aAbBcCdDeEfF"):
			print("Error non Hexa value found:", c)
			exit(1)

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--path', type=str)
parser.add_argument('-g', '--path', type=str)

password = getpass.getpass("Password: ")