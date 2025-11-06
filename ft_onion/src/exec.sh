#!/bin/bash
set -e
service ssh start
service tor start
nginx -g "daemon off;"