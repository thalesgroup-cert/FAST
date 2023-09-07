#!/usr/bin/python3
#Filename : FAST.py

import tkinter as tk
from Json import windowsSoftware, ubuntuSoftware
from Classes import Setting, Software, Detail

#Size of the window
posX = 200
posY = 200
width = 380
height = 400

#Set the title and the size
def createWindow():
    """This function creates a new windows with de width, height and position given"""
    window = tk.Tk()
    window.title("FAST")
    pos = str(width) + 'x' + str(height) + '+' + str(posX) + '+' + str(posY) 
    window.geometry(pos)
    window.resizable(False, False)
    return window

def radioButton(window, text, var, nb, command):
    """This function create a radio button on the selected window"""
    tk.Radiobutton(window,
            text = text, variable = var, value = nb,
            padx = 20, pady = 3, command = command).pack(side = "left")

def getSoftwareInformation(soft, mode, setting):
    opt = soft[mode]
    active = soft[mode]["active"]
    option = (
            opt["install"]["path"] if opt["install"]["active"] else "",
            opt["update"]["path"] if opt["update"]["active"] else "",
            opt["remove"]["path"] if opt["remove"]["active"] else ""
        )
    dependancies = []
    dep = opt["dependancies"]
    if dep["active"]:
            for name in dep["software"]:
                    nameSoftware = [mySoft.name for mySoft in setting.softwares]
                    if name in nameSoftware:
                            dependancies.append(setting.softwares[nameSoftware.index(name)])
    return option, active, dependancies

def main():
    #Create Windows and Setting Frame
    window = createWindow()
    setting = Setting()

    #Create software frame
    softwareFrame = tk.LabelFrame(window, text = "SOFTWARE")
    softwareFrame.pack(fill = "both", side = "top")

    #Create mode frame with each radiobox
    modeFrame = tk.LabelFrame(window, text = "MODE")
    modeFrame.pack(fill = "both", side = "top")

    radioButton(modeFrame, "Install", setting.tkMode, 0, setting.getMode)
    radioButton(modeFrame, "Update", setting.tkMode, 1, setting.getMode)
    radioButton(modeFrame, "Remove", setting.tkMode, 2, setting.getMode)
    
    #Create password Frame
    passwordFrame = tk.LabelFrame(window, text = "PASSWORD") if setting.system == 0 else tk.LabelFrame(window, text = "WSL PASSWORD")
    passwordFrame.pack(fill = "both", side = "top")
    password = tk.Entry(passwordFrame, show = "•", width = 45)
    if setting.system == 1:
        password.insert(0, "root")
    password.pack()
    setting.passFrame = password
    #setting.passFrame.config(state="disabled")

    #Create submit button
    submit = tk.Button(window, text = "SUBMIT",
            command = lambda:setting.validate(password)).pack()

    #Create detail frames
    detailFrame = Detail("DETAIL", window)
    detailFrame.init()
    
    osSoftware = ubuntuSoftware if setting.system == 0 else windowsSoftware
    for soft in osSoftware:
        optionUbuntu, activeUbuntu, depUbuntu = getSoftwareInformation(soft, "ubuntu", setting)
        optionWindows, activeWindows, depWindows = getSoftwareInformation(soft, "windows", setting)
        Software(soft["name"], soft["path"], (optionUbuntu, optionWindows), (activeUbuntu, activeWindows), (depUbuntu, depWindows), (softwareFrame, detailFrame), setting)

    setting.displayCheckbox()
    window.mainloop()

if __name__ == "__main__":
    main()
