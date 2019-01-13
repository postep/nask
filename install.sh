!/bin/bash

echo Update and install SNORT
apt-get update
apt-get -y install -y build-essential libncurses5-dev curl
apt-get -y install libcrypt-ssleay-perl liblwp-protocol-https-perl
export DEBIAN_FRONTEND=noninteractive
apt-get -yq install snort
