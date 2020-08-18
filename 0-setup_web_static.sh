#!/usr/bin/env bash
#deploy web_static for web server
if ! command -v nginx &> /dev/null
then
    apt -y update
    apt install -y nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Test Static deployement" > /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ]
then
    rm /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
echo "
server {
  listen 80;
  listen [::]:80 default_server;
  location /hbnb_static {
    alias /data/web_static/current/;
  }
  index index.html;
}" > /etc/nginx/sites-available/default
service nginx restart
