#!/bin/bash


NAME=$(wget -qO- https://github.com/sans-dfir/sift-cli/releases/latest | grep -Eo "teamdfir/sift-cli/releases/download/[a-zA-Z0-9./?=_-]*" | head -1)
echo "Start downloading sift-cli-linux from https://github.com/$NAME"
wget "https://github.com/$NAME" -q --progress=bar
echo "Download is finished !"

# Download key
echo $1 | sudo -S curl -fsSL -o /usr/share/keyrings/salt-archive-keyring.gpg https://repo.saltproject.io/py3/ubuntu/20.04/amd64/latest/salt-archive-keyring.gpg
# Create apt sources list file
echo "deb [signed-by=/usr/share/keyrings/salt-archive-keyring.gpg arch=amd64] https://repo.saltproject.io/py3/ubuntu/20.04/amd64/latest focal main" > salt.list
echo $1 | sudo -S mv ./salt.list /etc/apt/sources.list.d/salt.list
echo $1 | sudo -S apt update
echo $1 | sudo -S apt upgrade
echo $1 | sudo -S apt autoremove

# Move the file to "sift" directory
echo $1 | sudo -S cp sift-cli-linux /usr/local/bin/sift

# Give the right to acces to the file
echo $1 | sudo -S chmod 755 /usr/local/bin/sift

# Install SIFT
echo $1 | sudo -S sift install