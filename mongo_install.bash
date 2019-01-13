#!/bin/bash

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
sudo apt-get update
sudo apt-get install -y mongodb python3-pymongo
sudo cp -f /vagrant/mongodb.conf /etc/
sudo service mongodb restart

