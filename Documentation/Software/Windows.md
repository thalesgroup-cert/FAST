# Windows  
  
Version : Windows 10 (system 64x) version 20H2  
Softwares : [Autopsy](<#Autopsy>), [Cyberchef](<#Cyberchef>), [Free Hex Editor](<#Free Hex Editor>), [Remnux](<#Remnux>), [Sift](<#Sift>), [Wireshark](<#Wireshark>), [Wsl2](<#Wsl2>)  
  
### Autopsy  
  
Functionalities : install, update, remove  
Usage : You have a shortcut in the desktop  
  
  
### Cyberchef  
  
Functionalities : install, update, remove  
Usage : You have a shortcut in the desktop  
  
  
### Free Hex Editor  
  
Functionalities : install, update, remove  
Usage : You have a shortcut in the desktop  
  
  
### Remnux  
  
Functionalities : install, update  
Usage : Type `wsl` in a terminal, then you have a Remnux environment in the command prompt  
#### Troubleshooting  
  
##### Error : `$'\r': command not found`  
  
The script is used for both operating system windows and ubuntu. So it could be some error of comptability when you change the file in Ubuntu. In fact, when you save a file from Ubuntu, it create a newline character at the end and that's not compatible in Windows. To solve this problem, you should write in command line `wsl sed -i 's/$//' path/to/script/filename.sh`  
[https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile](<https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile>)  
Dependancies : Wsl2  
  
### Sift  
  
Functionalities : install, update  
Usage : Type `wsl` in a terminal, then you have a Sift environment in the command prompt  
#### Troubleshooting  
  
##### Error : `$'\r': command not found`  
  
The script is used for both operating system windows and ubuntu. So it could be some error of comptability when you change the file in Ubuntu. In fact, when you save a file from Ubuntu, it create a newline character at the end and that's not compatible in Windows. To solve this problem, you should write in command line `wsl sed -i 's/$//' path/to/script/filename.sh`  
[https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile](<https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile>)  
Dependancies : Wsl2  
  
### Wireshark  
  
Functionalities : install, update  
Usage : You have a shortcut in the desktop  
  
  
### Wsl2  
  
Functionalities : install, update  
Usage : Typing `wsl` in the terminal  
#### Troubleshooting  
  
##### Reboot system for installation  
  
If you launch the script and then nothing happened, you may reboot your system  
##### Error 0x80370102 : Activate virtualization  
  
This error occurs when the virtualization isn't activated in your virtual machine. To solve the problem, you have to activate it from VmWare or VirtualBox.  
[<img src=../Troubleshooting/Wsl/Wsl_virtualization_error.png width="300"/>](../Troubleshooting/Wsl/Wsl_virtualization_error.png)  
[<img src=../Troubleshooting/Wsl/Wsl_virtualization_solution.png width="300"/>](../Troubleshooting/Wsl/Wsl_virtualization_solution.png)  
[https://www.tactig.com/enable-intel-vt-x-amd-virtualization-pc-vmware-virtualbox/](<https://www.tactig.com/enable-intel-vt-x-amd-virtualization-pc-vmware-virtualbox/>)  
  
  
