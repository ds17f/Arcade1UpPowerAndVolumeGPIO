#!/bin/bash

set -x

# Copy the python scripts to the bin dir so that they 
# are in a place where the init scripts can find them
cp ./power.py /usr/local/bin
cp ./volume.py /usr/local/bin

# enable execute on  scripts
chmod +x /usr/local/bin/power.py
chmod +x /usr/local/bin/volume.py

# Install the init scripts
cp ./init_scripts/listen-for-shutdown.sh /etc/init.d
cp ./init_scripts/listen-for-volume.sh /etc/init.d

# enable execute on init scripts
chmod +x /etc/init.d/listen-for-shutdown.sh
chmod +x /etc/init.d/listen-for-volume.sh

# activate the init scripts so you don't have to reboot to have them working
/etc/init.d/listen-for-shutdown.sh start
/etc/init.d/listen-for-volume.sh start

# Enable the init scripts so that they run on startup
update-rc.d listen-for-shutdown.sh defaults
update-rc.d listen-for-volume.sh defaults

