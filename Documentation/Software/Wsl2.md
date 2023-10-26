# Wsl2  
  
Version : 2  
Last update : 2023-10-25  
Usage : It's a Windows Subsystems, it means that you can install an Ubuntu terminal in Windows  
Documentation : https://docs.microsoft.com/en-us/windows/wsl/  
  
Usable in Windows  
Path : Softwares/Wsl2  
  
### Windows  
  
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
  
  
##### Install  
  
File : installWsl2.bat  
Comment : Make sure to activate virtualization in your virtual machine (see troubleshooting)  
  
##### Update  
  
File : updateWsl2.bat  
  
