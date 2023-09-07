#!/usr/bin/python3
#Filename : Classes.py

import platform
import tkinter as tk
import subprocess
from subprocess import PIPE
import sys
import os

class Setting(object):
    def __init__(self):
        self.system = 0 if (platform.system() == "Linux") else 1
        self.password = ""
        self.passFrame = None
        self.tkMode = tk.IntVar()
        self.mode = 0
        self.softwares = []
        self.softwaresChecked = []
    
    def getMode(self):
        self.mode = self.tkMode.get()
        for soft in self.softwares:
            if len(soft.path[self.mode]) > 0:
                soft.button["state"] = "normal"
            else:
                soft.var.set(False)
                soft.button["state"] = "disabled"

    def displayCheckbox(self):
        pos = 0
        for soft in self.softwares:
            soft.checkButton(pos, soft.frameParent, self)
            pos = pos + 1

    def wslPassword(self):
        """Check if a software is using wsl as dependencies"""
        for soft in self.softwaresChecked:
            if ("Wsl2" in [s.name for s in soft.dep]):
                return True
        return False
    
    def getSoftwaresChecked(self):
        """Put all the checked softwares in a list"""
        self.softwaresChecked = [soft for soft in self.softwares if soft.checked()]

    def setPasswordState(self):
        """Update the state of the PasswordFrame"""
        if self.system == 1:
            self.getSoftwaresChecked()
            if (self.wslPassword()):
                self.passFrame.config(state="normal")
            else:
                self.passFrame.config(state="disabled")

    def validate(self, password):
        self.getSoftwaresChecked()
        self.password = password.get()
        if self.system == 0:
            if (len(self.softwaresChecked) > 0):
                soft = self.softwaresChecked[0]
                if (soft.putPassword(soft.frameMessage, self.password, self.system)):
                    self.launchApp()
        elif self.system == 1:
            if (self.wslPassword()):
                soft = self.softwaresChecked[0]
                wsl = [soft for soft in self.softwares if soft.name == "Wsl2"][0]
                wsl.launch(wsl.frameMessage, self.mode, self.password, self.system)
                if (soft.putPassword(soft.frameMessage, self.password, self.system)):
                    self.launchApp()
            else:
                self.launchApp()

    def launchApp(self):
        """Install or update all the software checked and make sure to install dependencies before"""
        for soft in self.softwares:
            if (soft.checked()):
                if (self.mode == 0):
                    #Install the dependencies if it's for an installation
                    for s in soft.dep:
                        s.launch(s.frameMessage, self.mode, self.password, self.system)
                soft.launch(soft.frameMessage, self.mode, self.password, self.system)

class Software(object):
    def __init__(self, name, directory, path, sys, dep, frame, setting):
        self.name = name
        self.var = tk.BooleanVar()
        self.directory = directory
        self.path = path[setting.system]
        self.dep = dep[setting.system]
        self.frameParent = frame[0]
        self.frameMessage = frame[1]
        if (sys[setting.system]):
            setting.softwares.append(self)
        self.mainPath = os.getcwd()

    def checked(self):
        """Check if the checkbox is checked"""
        return self.var.get()

    def checkButton(self, nb, frame, setting):
        """Display the checkbox with the software name"""
        self.button = tk.Checkbutton(frame,
                text = self.name, variable = self.var,
                onvalue = True, offvalue = False,
                command = setting.setPasswordState)
        self.button.grid(row = nb // 3, column = nb % 3, sticky = "NW")

    def putPassword(self, frameMessage, password, system):
        """Allow the program to do admin task"""
        command = 'echo "Password is correct !"'
        if system == 0:
            res = subprocess.call('echo {} | sudo -S {}'.format(password, command), shell=True)
        else:
            res = subprocess.call('wsl.exe echo {} ^| sudo -S {}'.format(password, command), shell=True)
        if (res == 1):
            frameMessage.addMessage("Your password is incorrect !")
        return True if res == 0 else False
    
    def launch(self, frameMessage, mode, password, system):
        os.chdir(self.mainPath)
        try:
            os.chdir(self.directory)
        except:
            print("Can't find the path for", self.name)
            os.chdir(self.mainPath)
            return
        if (self.path[mode].split(".")[-1] == "sh" or self.path[mode].split(".")[-1] == "bat"):
            self.launchBash(frameMessage, mode, password, system)
        elif (self.path[mode].split(".")[-1] == "py"):
            self.launchPython(frameMessage, mode, password, system)

    def launchBash(self, frameMessage, mode, password, system):
        if system == 0:
            script = ["bash " + self.path[mode], password]
        elif system == 1 and "Wsl2" in [s.name for s in self.dep]:
            script = ["wsl.exe", "bash", self.path[mode], password]
        else:
            script = ["call", self.path[mode]]
        process = subprocess.Popen(script, stderr = PIPE, shell = True)
        stdout, stderr = process.communicate()

        stderr = stderr.decode('utf-8', errors = "ignore")
        if (len(stderr) > 0):
            txt_error = "ERROR " + self.name + ":\n" + stderr[:-1]
            frameMessage.addMessage(txt_error)
        else:
            if mode == 0:
                frameMessage.addMessage("INSTALLED: " + self.name)
            elif mode == 1:
                frameMessage.addMessage("UPDATED: " + self.name)
            elif mode == 2:
                frameMessage.addMessage("REMOVED: " + self.name)

    def launchPython(self, frameMessage, mode, password, system):
        for path, subdirs, files in os.walk("."):
            for filename in files:
                if filename == "requirements.txt":
                    subprocess.run(["pip3", "install", "-r", "requirements.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        className = self.path[mode][:-3]
        mod = ".".join(self.directory.split("/")) + "." + className
        module = __import__(mod, fromlist=[className])
        classSoft = getattr(module, className)
        mySoft = classSoft(self)

        if mode == 0:
            if (mySoft.isInstalled()): 
                frameMessage.addMessage(self.name + " is already installed!")
            else:
                mySoft.install()
                if not mySoft.result['error']:
                    frameMessage.addMessage("INSTALLED: " + self.name)
        elif mode == 1:
            mySoft.update()
            frameMessage.addMessage("UPDATED: " + self.name)
        elif mode == 2:
            mySoft.remove()
            frameMessage.addMessage("REMOVED: " + self.name)
        if mySoft.result['error']:
            for err in mySoft.result['errorMessage']:
                frameMessage.addMessage(err)



class Detail(object):
    def __init__(self, name, frame):
        self.name = name
        self.frame = tk.LabelFrame(frame, text = name)
        self.sb = tk.Scrollbar(self.frame, orient = 'vertical')
        self.message = tk.Text(self.frame, yscrollcommand = self.sb.set)

    def init(self):
        self.frame.pack(fill = "both", expand = "yes", side = "bottom")
        self.sb.pack(side="right", fill='y')
        self.sb.config(command = self.message.yview)
        self.message.pack()
        self.message.configure(state = 'disabled')
        self.message.tag_configure("center", justify = 'center')

    def addMessage(self, mess):
        self.message.configure(state = 'normal')
        self.message.insert("end", "\n" + mess)
        self.message.tag_add("center", "1.0", "end")
        self.message.configure(state = 'disabled')
        self.message.see("end")