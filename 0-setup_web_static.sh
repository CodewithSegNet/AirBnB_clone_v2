#!/usr/bin/env bash
# Bash Scripot to set up web servers for web_static deployment
sudo apt-get install update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# create index.html for test directory
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# give user ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# backup default server config file
sudo cp /etc/nginx/sites-enabled/default nginx-sites-enabled_default.backup

# Set-up the content of /data/web_static/current/ to redirect
# to domain.tech/hbnb_static
sudo sed -i '37i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
