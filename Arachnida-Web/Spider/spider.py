# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yitani <yitani@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/03 23:11:05 by yitani            #+#    #+#              #
#    Updated: 2025/11/04 09:28:20 by yitani           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from sys import argv
import requests
import os

def	imgDownload(url, images):
	for img in images:
		global index
		imageSrc = img.get("src")
		if not imageSrc:
			continue

		full_url = urljoin(url, imageSrc)
		parsed_url = urlparse(full_url)

		try:
			image_response = requests.get(full_url)
			image_data = image_response.content
		except requests.exceptions.RequestException as e:
			print("Error fetching the image URL:", e)
		
		fileName = os.path.basename(parsed_url.path)
		if not fileName.endswith((".jpg","jpeg",".png",".gif",".bmp")):
			continue

		print("Downloading img: " + fileName)
		try:
			file = open(os.path.join(path, str(index)+"-"+fileName), "wb")
			file.write(image_data)
			file.close()
		except Exception:
			continue
		index += 1

def	extractLinks(url, refs, curr_depth):
	for link in refs:
		hrefs = link.get("href")
		if not hrefs:
			continue
		if hrefs.startswith(("javascript:", "mailto:", "#", "tel:")):
			continue
		full_link = urljoin(url, hrefs)
		if full_link in visitedURL:
			continue
		if urlparse(full_link).netloc == base_domain and urlparse(full_link).scheme in ["https", "http"]:
			spider(full_link, curr_depth + 1)

def	spider(url, curr_depth=0):
	if url in visitedURL or (curr_depth > maxDepth and recursive):
		return
	visitedURL.add(url)

	try:
		response = requests.get(url)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		print("Error fetching the page:", e)

	print("currently scrapping", url)
	soup = BeautifulSoup(response.text, "html.parser")
	images = soup.find_all("img")
	refs = soup.find_all("a")
	imgDownload(url, images)
	if recursive:
		extractLinks(url, refs, curr_depth)

index = 0
visitedURL = set()
parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL to scrape")
parser.add_argument("-r", "--recursive", action="store_true", help="Recursively download images")
parser.add_argument("-p", "--path", type=str, default="./data/", help="Path to save files, default=./data/")
parser.add_argument("-l", "--maxDepth", type=int, default=5, help="Maximum depth level, default=5")

args = parser.parse_args()
url = args.url
path = args.path
maxDepth = args.maxDepth
recursive = args.recursive
base_domain = urlparse(url).netloc

if "-l" in argv and not recursive:
	print("Error: -l requires -r flag")
	exit(1)

os.makedirs(path, exist_ok=True)

try:
	spider(url)
except KeyboardInterrupt:
	print("\nspider interrupted by user")
	exit(1)