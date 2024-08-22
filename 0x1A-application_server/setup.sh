#!/usr/bin/env bash
# This script installs Gunicorn, Flask, and configures Nginx for the AirBnB clone application.

# Update package lists
sudo apt-get update

# Install necessary packages
sudo apt-get install -y python3-pip nginx

# Install Python packages
pip3 install gunicorn flask

# Copy the Nginx configuration file
sudo cp 2-app_server-nginx_config /etc/nginx/sites-available/default

# Restart Nginx to apply the configuration
sudo systemctl restart nginx

echo "Setup complete. Nginx and Gunicorn have been configured."