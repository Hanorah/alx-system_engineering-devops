#!/usr/bin/env bash

# Update the user directive in the nginx configuration file
sed -i 's/user www-data;/user nginx;/' /etc/nginx/nginx.conf

# Restart the Nginx service
service nginx restart
