#!/usr/bin/env bash
# Bash Scripot to set up web servers for web_static deployment
sudo apt-get install update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Update Nginx configuration
sudo sed -i 's#location \/ \{#location \/hbnb_static\/ \{#g' /etc/nginx/sites-available/default

sudo sed -i 's#alias \/data\/web_static\/html\/\;#alias \/data\/web_static\/current\/\;\n\tindex index.html\;#g' /etc/nginx/sites-available/default

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '39 i\   \tlocation /new_static {\n\talias /data/web_static/current;\n}' /etc/nginx/sites-available/default

sudo service nginx restart
