@ECHO OFF

wsl [[ $USER = "user" ]] && goto alreadyInstall 
wsl --install
wsl --install -d Ubuntu
timeout 120
ubuntu config --default-user root
wsl adduser --disabled-password --gecos "" user
wsl echo user:root ^| chpasswd
wsl usermod -a -G sudo user
ubuntu config --default-user user

:alreadyInstall
echo "Ubuntu is installed !"