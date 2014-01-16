#!/bin/bash

echo "Downloading screenly-manager..."
git clone git://github.com/svdgraaf/screenly-manager.git ~/screenly-manager > /dev/null

echo "Installing packages"
sudo apt-get -qq update > /dev/null
sudo apt-get -y -qq install libnss-mdns libavahi-compat-libdnssd1 > /dev/null
sudo pip install pybonjour > /dev/null

echo "Adding Screenly to autostart (via Supervisord)"
sudo ln -sfT ~/screenly-manager/supervisor_bonjour.conf /etc/supervisor/conf.d/screenly_bonjour.conf
sudo /etc/init.d/supervisor stop > /dev/null
sudo /etc/init.d/supervisor start > /dev/null

echo "Done"