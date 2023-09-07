import json
import os

softDirectory = "../Softwares"
docDirectory = "../Documentation/Software"
software = []
windowsSoftware = []
ubuntuSoftware = []

def getAllSoftware(directory):
    for path, subdirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".json"):
                soft = os.path.join(path, filename)
                try:
                    with open(soft, "r") as read_file:
                        s = json.load(read_file)
                    if s["active"]:
                        software.append(s)
                    if s["active"] and s["windows"]["active"]:
                        windowsSoftware.append(s)
                    if s["active"] and s["ubuntu"]["active"]:
                        ubuntuSoftware.append(s)
                except:
                    print("Fail to read", soft)


def w_ret():
    return "  \n"

def w_title(title, level):
    txt = "#" * level
    txt += " " + title + "  \n"
    return txt

def w_link(title, link, ref):
    txt = "[" + title + "]" + "(<"
    if ref:
        txt += "#"
    txt += link + ">)"
    return txt

def w_img(src):
    txt = "[<img src=" + src + " width=\"300\"/>](" + src + ")" + w_ret()
    return txt


def w_bullet(txt):
    return "- " + txt


def get_general_info(soft):
    txt = "Version : " + soft["version"] + w_ret()
    txt += "Last update : " + soft["lastUpdate"] + w_ret()
    txt += "Usage : " + soft["usage"] + w_ret() if len(soft["usage"]) > 0 else ""
    txt += "Documentation : " + soft["doc"] + w_ret() + w_ret() if len(soft["doc"]) > 0 else w_ret()
    return txt

def get_usable(soft):
    usable = (1 if soft["ubuntu"]["active"] else 0, 1 if soft["windows"]["active"] else 0)
    if (usable == (1, 1)):
        txt = "Usable in Ubuntu and Windows"
    elif (usable == (1, 0)):
        txt = "Usable in Ubuntu"
    elif (usable == (0, 1)):
        txt = "Usable in Windows"
    return txt + w_ret()

def get_troubleshooting(soft, os):
    if len(soft[os]["troubleshooting"]) == 0:
        return ""
    txt = w_title("Troubleshooting", 4) + w_ret()
    for ts in soft[os]["troubleshooting"]:
        txt += w_title(ts["title"], 5) + w_ret()
        txt += ts["description"] + w_ret()
        for src in ts["images"]:
            txt += w_img("../Troubleshooting/" + src)
        for link in ts["link"]:
            txt += w_link(link, link, False)
    return txt + w_ret()

def get_os_info(soft, os):
    txt = "Functionalities : "
    txt += "install" if soft[os]["install"]["active"] else ""
    txt += ", update" if soft[os]["update"]["active"] else ""
    txt += ", remove" + w_ret() if soft[os]["remove"]["active"] else w_ret()
    txt += "Usage : " + soft[os]["usage"] + w_ret() if len(soft[os]["usage"]) > 0 else ""
    txt += get_troubleshooting(soft, os)
    txt += "Dependancies : " if len(soft[os]["dependancies"]["software"]) > 0 else ""
    if len(soft[os]["dependancies"]["software"]) > 0:
        txt += soft[os]["dependancies"]["software"][0]
    for name in soft[os]["dependancies"]["software"][1:]:
        txt += ", " + name
    return txt + w_ret() + w_ret()

def get_os_func(soft, os, title, mode):
    txt = ""
    if soft[os][mode]["active"]:
        txt += w_title(title, 5) + w_ret()
        txt += "File : "+ soft[os][mode]["path"] + w_ret()
        txt += "Comment : "+ soft[os][mode]["comment"] + w_ret() + w_ret() if len(soft[os][mode]["comment"]) > 0 else w_ret()
    return txt

def create_md_software(soft, directory):
    path = directory + "/" + soft["name"] + ".md"
    with open(path, "w") as f:
        f.write(w_title(soft["name"], 1) + w_ret())
        f.write(get_general_info(soft))
        f.write(get_usable(soft))
        f.write("Path : " + soft["path"] + w_ret() + w_ret())
        if soft["ubuntu"]["active"]:
            f.write(w_title("Ubuntu", 3) + w_ret())
            f.write(get_os_info(soft, "ubuntu"))
            f.write(get_os_func(soft, "ubuntu", "Install", "install"))
            f.write(get_os_func(soft, "ubuntu", "Update", "update"))
            f.write(get_os_func(soft, "ubuntu", "Remove", "remove"))
        if soft["windows"]["active"]:
            f.write(w_title("Windows", 3) + w_ret())
            f.write(get_os_info(soft, "windows"))
            f.write(get_os_func(soft, "windows", "Install", "install"))
            f.write(get_os_func(soft, "windows", "Update", "update"))
            f.write(get_os_func(soft, "windows", "Remove", "remove"))

def get_soft_list(softwares):
    if len(softwares) == 0:
        return ""
    txt = "Softwares : " + w_link(softwares[0]["name"], softwares[0]["name"], True)
    for soft in softwares[1:]:
        txt += ", " + w_link(soft["name"], soft["name"], True)
    return txt + w_ret() + w_ret()

def create_md_list(softwares, directory):
    ubuntu_path = directory + "/Ubuntu.md"
    windows_path = directory + "/Windows.md"
    soft_list_ubuntu = get_soft_list(ubuntuSoftware)
    soft_list_windows = get_soft_list(windowsSoftware)

    with open(ubuntu_path, "w") as f:
        f.write(w_title("Ubuntu", 1) + w_ret())
        f.write("Version : Ubuntu 20.04.3 LTS (64-bit)" + w_ret())
        f.write(soft_list_ubuntu)
        for soft in software:
            if soft["ubuntu"]["active"]:
                f.write(w_title(soft["name"], 3) + w_ret())
                f.write(get_os_info(soft, "ubuntu"))
            
    with open(windows_path, "w") as f:
        f.write(w_title("Windows", 1) + w_ret())
        f.write("Version : Windows 10 (system 64x) version 20H2" + w_ret())
        f.write(soft_list_windows)
        for soft in software:
            if soft["windows"]["active"]:
                f.write(w_title(soft["name"], 3) + w_ret())
                f.write(get_os_info(soft, "windows"))

getAllSoftware(softDirectory)
software = sorted(software, key=lambda x: x['name'])
ubuntuSoftware = sorted(ubuntuSoftware, key=lambda x: x['name'])
windowsSoftware = sorted(windowsSoftware, key=lambda x: x['name'])
create_md_list(software, docDirectory)
for soft in software:
    create_md_software(soft, docDirectory)
#print(software)
