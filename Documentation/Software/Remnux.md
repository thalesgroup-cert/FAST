# Remnux  
  
Version : v2021.41.1  
Last update : 2022-08-17  
Usage : Remnux is a Linux toolkit for reverse-engineering and analyzing malicious software. It provides a curated collection of free tools created by the community.  
Documentation : https://docs.remnux.org/  
  
Usable in Ubuntu and Windows  
Path : Softwares/REMnux  
  
### Ubuntu  
  
Functionalities : install, update  
Usage : It's directly in the prompt command  
  
  
##### Install  
  
File : installREMnux.sh  
  
##### Update  
  
File : updateREMnux.sh  
  
### Windows  
  
Functionalities : install, update  
Usage : Type `wsl` in a terminal, then you have a Remnux environment in the command prompt  
#### Troubleshooting  
  
##### Error : `$'\r': command not found`  
  
The script is used for both operating system windows and ubuntu. So it could be some error of comptability when you change the file in Ubuntu. In fact, when you save a file from Ubuntu, it create a newline character at the end and that's not compatible in Windows. To solve this problem, you should write in command line `wsl sed -i 's/$//' path/to/script/filename.sh`  
[https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile](<https://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile>)  
Dependancies : Wsl2  
  
##### Install  
  
File : installREMnux.sh  
  
##### Update  
  
File : updateREMnux.sh  
  
