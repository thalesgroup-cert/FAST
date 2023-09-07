import json
import os
import copy
from datetime import datetime

directory = "Softwares"
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
                        software.append((soft, copy.deepcopy(s)))
                    if s["active"] and s["windows"]["active"]:
                        windowsSoftware.append(s)
                    if s["active"] and s["ubuntu"]["active"]:
                        ubuntuSoftware.append(s)
                except:
                    print("Fail to read", soft)


def getPrioritySoftware(soft, tab, mode):
    priority = 0
    softDep = soft[mode]["dependancies"]
    if softDep["active"]:
        priority += len(softDep["software"])
        for name in softDep["software"]:
            if name in [soft["name"] for soft in windowsSoftware]:
                ind = [soft["name"] for soft in windowsSoftware].index(name)
                priority += getPrioritySoftware(tab[ind], tab, mode)
    return priority


getAllSoftware(directory)

for soft in windowsSoftware:
    priority = getPrioritySoftware(soft, windowsSoftware, "windows")
    soft["windows"]["priority"] = priority + 100 if soft["end"] else priority

for soft in ubuntuSoftware:
    priority = getPrioritySoftware(soft, ubuntuSoftware, "ubuntu")
    soft["ubuntu"]["priority"] = priority + 100 if soft["end"] else priority

windowsSoftware = sorted(windowsSoftware, key = lambda item: item["windows"]["priority"])
ubuntuSoftware = sorted(ubuntuSoftware, key = lambda item: item["ubuntu"]["priority"])

def lastUpdateDate(path, filename, lastUpdate):
    os.chdir(os.path.join(mainPath, path))
    update = os.path.getmtime(filename)
    update_datetime = datetime.fromtimestamp(update)
    if update_datetime > lastUpdate:
        return update_datetime
    else:
        return lastUpdate

mainPath = os.getcwd()

for filepath, soft in software:
    lastUpdate = datetime.strptime(soft["lastUpdate"], "%Y-%m-%d")
    tabWindows = [soft["windows"]["install"], soft["windows"]["update"], soft["windows"]["remove"]]
    tabUbuntu = [soft["ubuntu"]["install"], soft["ubuntu"]["update"], soft["ubuntu"]["remove"]]
    if soft["windows"]["active"]:
        for softMode in tabWindows:
            if softMode["active"]:
                lastUpdate = lastUpdateDate(soft["path"], softMode["path"], lastUpdate)
    if soft["ubuntu"]["active"]:
        for softMode in tabUbuntu:
            if softMode["active"]:
                lastUpdate = lastUpdateDate(soft["path"], softMode["path"], lastUpdate)
    soft["lastUpdate"] = lastUpdate.strftime("%Y-%m-%d")
    finalPath = os.path.join(mainPath, filepath)
    with open(finalPath, "w") as js:
        json.dump(soft, js, indent = 4)

os.chdir(mainPath)