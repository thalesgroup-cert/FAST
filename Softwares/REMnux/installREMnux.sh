#!/bin/bash

echo "Start downloading sift-cli-linux from https://REMnux.org/remnux-cli"
wget "https://REMnux.org/remnux-cli" -q --progress=bar
echo "Download is finished !"

# Give the right to acces to the file and move the installer file to the root
if [ -f "Softwares/REMnux/remnux-cli" ]; then
	echo $1 | sudo -S chmod +x Softwares/REMnux/remnux-cli
	echo $1 | sudo -S cp Softwares/REMnux/remnux-cli /usr/local/bin/remnux;
else
	echo $1 | sudo -S chmod +x ./remnux-cli
	echo $1 | sudo -S cp ./remnux-cli /usr/local/bin/remnux;
fi

# Install GnuPG
echo $1 | sudo -S apt install -y gnupg

# Install remnux
echo $1 | sudo -S remnux install
