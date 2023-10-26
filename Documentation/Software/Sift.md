# Sift  
  
Version : v2021.9.1  
Last update : 2023-10-25  
Usage : The SIFT Workstation is a collection of free and open-source incident response and forensic tools designed to perform detailed digital forensic examinations in a variety of settings. It can match any current incident response and forensic tool suite.  
Documentation : https://www.sans.org/tools/sift-workstation/  
  
Usable in Ubuntu and Windows  
Path : Softwares/Sift  
  
### Ubuntu  
  
Functionalities : install, update  
Usage : It's directly in the prompt command  
  
  
##### Install  
  
File : installSift.sh  
  
##### Update  
  
File : updateSift.sh  
  
### Windows  
  
Functionalities : install, update  
Usage : Type `wsl` in a terminal, then you have a Sift environment in the command prompt  
#### Troubleshooting  
  
##### Error : `$'\r': command not found`  
  
The script is used for both operating system windows and ubuntu. So it could be some error of comptability when you change the file in Ubuntu. In fact, when you save a file from Ubuntu, it create a newline character at the end and that's not compatible in Windows. To solve this problem, you should write in command line `wsl sed -i 's/$//' path/to/script/filename.sh`  
[https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile](<https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile>)  
Dependancies : Wsl2  
  
##### Install  
  
File : installSift.sh  
  
##### Update  
  
File : updateSift.sh  
  
