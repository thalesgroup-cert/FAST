#!/bin/bash

sudo apt-get -y update
sudo apt-get -y upgrade

#Install python3 if necessary
if !(command -v python3 >/dev/null 2>&1)
then
	pkexec apt-get -y install python3
	sudo apt -y install python3-pip
fi

#Install tkinter if necessary
if !(command -v python3-tk >/dev/null 2>&1)
then
	pkexec apt-get -y install python3-tk
fi

pip3 install -r requirements.txt
cp -r ../Documentation/"CheatSheet SANS"  $(command xdg-user-dir DESKTOP)

cd ..
chmod -R 764 *