
# Developer documentation

The program main usage is to install many software without users' interaction. 
In this way, the user can launch FAST program to install softwares while doing something else until the installation finished.

This documentation will explain how the program works and how you can add or update a script software.

## Program structure
Below you can find the tree structure to understand the program composition

```
├── README.md
├── FAST.py
├── Classes.py
├── Json.py
├── Launch_Windows.bat
├── Setup
│   ├── ubuntu.sh
│   ├── windows.bat
│   └── build_md.py
├── Documentation
│   ├── CheatSheet SANS
│   │   ├── cheatsheet.pdf
│   │   └── ...
│   ├── Ressources
│   │   ├── ressources.png
│   │   └── ...
│   ├── Troubleshooting
│   │   ├── troubleshooting.png
│   │   └── ...
│   └── Software
│       ├── Autopsy.md
│       ├── Cyberchef.md
│       ├── ...
│       ├── Ubuntu.md
│       └── Windows.md
├── Tutorial
│   ├── Setup_ubuntu.mp4
│   ├── Tutorial.mkv
│   └── ...
└── Softwares
    ├── Example.json
    ├── Autopsy
    │   ├── installAutopsy.sh
    │   ├── installAutopsy.bat
    │   ├── updateAutopsy.bat
    │   ├── removeAutopsy.bat
    │   └── Autopsy.json
    ├── CyberChef
    │   ├── Cyberchef.py
    │   ├── requirements.txt
    │   └── Cyberchef.json
    └── ...
```

### Root tree files

In the tree root, you have the main script wrote in Python:
- `FAST.py` : the main program
- `Classes.py` : all the classes used (Setting, Software and Detail)
- `Json.py` : script search all JSON files in the `Softwares` directory and create a class to get all the scripts paths wrote in Json

A bash file called `Launch_Windows.bat` : the launching program for Windows.


### Setup directory
In the setup directory, you have the following files :
- `ubuntu.sh` : it install python and tkinter for ubuntu
- `windows.bat` : it install Winget and Tkinter for windows
- `build_md.py` : it will generate the documentation files in markdown for each software from the related JSON file, it generates a JSON files placed at `Documentation/Software`


### Documentation directory

#### Cheatsheet SANS
When the user launch the setup file for windows or ubuntu, it will copy all the SANS cheatsheet pdf file of this directory in the Desktop.

#### Ressources and Troubleshooting
There are many pictures used for the `readme.md` file, and pictures used for troubleshooting part in each software documentation.

#### Software
Here you will find a markdown file related to each software that you can install, but also two others files :
- `Ubuntu.md` : a summary of all the software that can be install in ubuntu operating system
- `Windows.md` : a summary of all the software that can be install in windows operating system

#### Tutorial
You can find short videos of how to setup and use the program for ubuntu and windows


### Software directory

In this directory you find a file called `Example.json`, i's explain the syntax of a json file. 
You also have a directory for each software you can install.

In each software directory, there is: 
- `JSON file (.json)` : it's one of the most important file, it's where you will specify what script to launch for each mode, and all the specificities of the installed software
- `Bash file (.sh or .bat) or Python file (.py)` : script file that the program will run to install, update or remove a software
- [optional] `Requirements file (requirements.txt)` : text file that will list all the python libraries to install before launching the python script file

You will find more about these file in the next part `How to add a software ?`.




## How to add a software?

To create a software, you need to create a directory with the software name in the `Softwares` directory, and add a json file and script file (python or bash).

### Structure of the JSON file
**This file is very important** because this is where you will specify all the features of the software. 
You can find a template in `Software > Example.json`.

This file will be used by two script :
- `build_md.py` in the `Setup` directory to generate the software documentation in `Documentation/Software`
- `Json.py` that create a `Software` class in python with all scripts paths related to this software


#### General fields
- `name` : name that will be displayed on the graphical interface
- `version` : version installed by the script
- `lastUpdate` (_YYYY-MM-DD_) : date of the last script change
- `active` (_True_ / _False_) : True if the program should be in production, False if it should be not (for testing purposes)
- `end`  (_True_ / _False_) : if the software should be installed at the end (that could be useful if your program reboot system, in this way it will install other software before installing this one)
- `usage` : short description of the software usage
- `doc` : link to the documentation
- `path` : path to the software folder

#### Windows and Ubuntu fields
For each operating system, you will find the same fields :
- `active` (_True_ / _False_) : if you can install this software on this operating system
- `usage` : the way you launch or run the software for the user

##### Install, update, remove
For each operating system, you have the fields : install, update and remove. Each of them have also three fields:
- `active` (_True_ / _False_) : if you can install, update or remove this software on this operating system
- `path` (_.sh_, _bat_, _.sh_) : the script filename to execute
- [optional] `comment` : a note explaining how to install, update or remove

##### Dependancies
Some software require other software being installed first. For example, you need to install WSL first, if you want to install remnux or sift in Windows. That's the purpose of this field, install another software before this one.

You will find two fields in dependancies fields : 
- `active`  (_True_ / _False_) : that indicate if the software have any dependancies
- `software` (_List of software names_) : list of software name you need (the name has to be exactly the same as the name in general field)


#### Troubleshooting
In windows or ubuntu fields, you have a part called troubleshooting that identify problems that you encounter and that the user might too.

IThis troubleshooting field is composed of a dictionnary list of four fields:
- `title` : troubleshooting title
- `description` : problem description
- `images` (_list_) : problem of solution screenshot (image source from the folder Documentation/Troubleshooting)
- `link` (_list_) : website link that solve or talk about the problem


### How to write the JSON file?
You need to specify the python or bash script file in the json file.

#### Python script example
```
Softwares
    ├── Example.json 
	├── mySoftware
    │   ├── mySoftware.py
    │   └── mySoftware.json
    └── ...
```

You have a python script at the path `Softwares/mySoftware/mySoftware.py` that could :
- `install` and `update` the software in `Windows`
- `update` the software in `Linux`

You need to fill some fields in the file `mySoftware.json` :
- `name` : mySoftware
- `active` : True
- `path` : Softwares/mySoftware

In Windows field :
- `windows > active` : True
- `windows > install > active` : True
- `windows > install > path` : mySoftware.py
- `windows > update > active` : True
- `windows > update > path` : mySoftware.py
- `windows > remove > active` : False

In Ubuntu field :
- `ubuntu > active` : True
- `ubuntu > install > active` : True
- `ubuntu > install > path` : mySoftware.py
- `ubuntu > update > active` : False
- `ubuntu > remove > active` : False


#### Bash script example

```
Softwares
    ├── Example.json 
    ├── MySoftware
    │   ├── installMySoftware.sh
    │   ├── installMySoftware.bat
    │   ├── updateMySoftware.sh
    │   └── MySoftware.json
    └── ...
```

You have many bash script :
- `install` in `windows` : `Softwares/mySoftware/installMySoftware.bat`
- `install` in `ubuntu` : `Softwares/mySoftware/installMySoftware.sh`
- `update` in `ubuntu` : `Softwares/mySoftware/installMySoftware.sh`

You need to fill some fields in the file `mySoftware.json`
- `name` : mySoftware
- `active` : True
- `path` : Softwares/mySoftware

In Windows field :
- `windows > active` : True
- `windows > install > active` : True
- `windows > install > path` : installMySoftware.bat
- `windows > update > active` : False
- `windows > remove > active` : False

In Ubuntu field :
- `ubuntu > active` : True
- `ubuntu > install > active` : True
- `ubuntu > install > path` : installMySoftware.sh
- `ubuntu > update > active` : True
- `ubuntu > update > path` : updateMySoftware.sh
- `ubuntu > remove > active` : False


### Create a script using Python

First you need to specify the script in the JSON file, please read the part `Structure of the JSON file` and `How to write the JSON file ?` to understand the JSON file structure.

```
Softwares
    ├── Example.json 
	├── mySoftware
    │   ├── mySoftware.py
    │   ├── requirements.txy
    │   └── mySoftware.json
    └── ...
```

#### Requirements.txt (Optional)
This file must be called `requirements.txt`. You will specify the python libraries that the program will install before executing the script.

Indeed, if you need `requests` and `pandas` libraries to execute your python script, you have to specifiy it in the `requirements.txt` file:
```
requests
pandas
```


#### Python script file

The python script file will only be composed by a class with install, update and remove methods. The name of the class has to be the same as the script file, it's `mySoftware` in our case.

There is an example of a python script file in the Cyberchef software.

##### Class initialization
The init method will always be the same
```
class mySoftware(object):
	def __init__(self, basic):
		self.basic = basic
		self.result = {
			"error": False,
			"errorMessage": []
		}
	...
```

##### Other class methods

The method `isInstalled` return _True_ or _False_ according to the software installation. If you didn't implement this functionality yet, you could just return _False_.

And then you have `install`, `update`, `remove` methods that respectively are the scripts to install, update and remove the software.


##### Display errors

In the initialization, you have two items in the `result` attribute :
- `error` (_False_) : you can change to _True_ if you encounter an error
- `errorMessage` (_List of message_) : you can add a message depending the error in each method `install`, `update`, and `remove`.

The message list in `errorMessage` will be printed in the graphical interface at the end of the installation.


### Create a script using Bash

First you need to specify the script in the JSON file, please read the part `Structure of the JSON file` and `How to write the JSON file ?` to understand the JSON file structure.

```
Softwares
    ├── Example.json 
	├── mySoftware
    │   ├── installMySoftware.sh
    │   └── mySoftware.json
    └── ...
```

In the bash script file `installMySoftware.sh`, you can write anything you want in bash code. However, notice that bash code is different from ubuntu and windows that's why their extension are respectively `.sh`(ubuntu) and `.bat`(windows).

In ubuntu, if you need administrator right to execute a code, you need to call the command with `sudo` in this way :
`echo $1 | sudo -S my_command`

In fact, in order to deal with ubuntu administrator right, the program will called the script as `bash Softwares/mySoftware/installMySoftware.sh adminPassword`


## How to update a software script?
### Find the associated script file from JSON file
From the JSON file in the software directory, you will check the file related to the script you want to update. The search filename will be on these fields :
- `ubuntu > install > path`
- `ubuntu > update > path`
- `ubuntu > remove > path`
- `windows > install > path`
- `windows > update > path`
- `windows > remove > path`

### Update a python script  file
```
Softwares
    ├── Example.json 
	├── mySoftware
    │   ├── mySoftware.py
    │   └── mySoftware.json
    └── ...
```

For example, if the file you want to update is `mySoftware.py`, then you can update the method `isIntalled`, `install`, `update` and `remove` from the class object.

### Update a bash script file
```
Softwares
    ├── Example.json 
    ├── MySoftware
    │   ├── installMySoftware.sh
    │   ├── installMySoftware.bat
    │   ├── updateMySoftware.sh
    │   └── MySoftware.json
    └── ...
```

For example, if the file you want to update is `installMySoftware.sh`, then you can update the script file.
However don't forget to use the syntax `echo $1 | sudo -S my_command` if you need administrator right.


