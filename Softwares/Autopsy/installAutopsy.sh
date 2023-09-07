#!/bin/bash
#Filename : installAutopsy.sh

#Install testdisk
sudo apt-get install testdisk

#Install BellSoft Java 8
wget -q -O - https://download.bell-sw.com/pki/GPG-KEY-bellsoft | sudo apt-key add -
echo "deb [arch=amd64] https://apt.bell-sw.com/ stable main" | sudo tee /etc/apt/sources.list.d/bellsoft.list
sudo apt-get update
sudo apt-get install -y bellsoft-java8-full
export JAVA_HOME=/usr/lib/jvm/bellsoft-java8-full-amd64

#Install sleuthkit.deb
[ -d "Softwares/Autopsy" ] && cd Softwares/Autopsy
wget https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-4.11.0/sleuthkit-java_4.11.0-1_amd64.deb
sudo apt install -y ./sleuthkit-java_4.11.0-1_amd64.deb


#Install Autopsy
wget https://github.com/sleuthkit/autopsy/releases/download/autopsy-4.19.1/autopsy-4.19.1.zip
unzip autopsy-4.19.1.zip -d ./
mv autopsy-4.19.1 autopsy
cd autopsy
sh unix_setup.sh
chmod +x bin/autopsy
cd ../

#Create alias for autopsy
sudo cp -r autopsy /usr/local/bin/
sudo chmod +x /usr/local/bin/autopsy/bin/autopsy
echo "alias autopsy='/usr/local/bin/autopsy/bin/autopsy'" >> ~/.bashrc
exec bash
