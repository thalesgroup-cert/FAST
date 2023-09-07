#!/bin/bash

echo "wireshark-common wireshark-common/install-setuid boolean true" | sudo debconf-set-selections
echo $1 | sudo DEBIAN_FRONTEND=noninteractive apt-get -y install wireshark