import platform
import requests
import re
import sys
import shutil
import os

class CyberChef(object):
    def __init__(self, basic):
        self.basic = basic
        self.result = {
            "error": False,
            "errorMessage": []
        }

    def isInstalled(self):
        userprofile = os.path.expanduser('~') if (platform.system() == "Linux") else os.environ['USERPROFILE']
        desktop = os.path.join(os.path.join(userprofile), 'Desktop')
        cyberchef_file = os.path.join(os.path.join(desktop), 'CyberChef.html')
        if os.path.exists(cyberchef_file):
            return True
        return False

    def install(self):
        def download_progression(url, filename):
            with open(filename, "wb") as f:
                print("Downloading %s" % filename)
                response = requests.get(url + filename, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None: # no content length header
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                        sys.stdout.flush()
            print("\nDownload finished !")

        regex = "CyberChef[a-zA-Z0-9./?=_-]*.zip"

        url = 'https://gchq.github.io/CyberChef/'
        html_text = requests.get(url).text
        filename = re.search(regex, html_text).group(0)
        download_progression(url, filename)

        #Unzip the archive
        new_folder = "CyberChef"
        shutil.unpack_archive(filename, new_folder)

        #Move the folder to the Desktop and add symbolic link
        try:
            userprofile = os.path.expanduser('~') if (platform.system() == "Linux") else os.environ['USERPROFILE']
            desktop = os.path.join(os.path.join(userprofile), 'Desktop') 
            shutil.move(new_folder, desktop)
            os.symlink(desktop + "/" + new_folder + "/" + filename[:-4] + ".html", desktop + "/" + new_folder + ".html")
        except Exception as e:
            self.result['error'] = True
            self.result['errorMessage'].append("Cyberchef error: " + str(e))

    def update(self):
        self.remove()
        self.install()

    def remove(self):
        userprofile = os.path.expanduser('~') if (platform.system() == "Linux") else os.environ['USERPROFILE']
        desktop = os.path.join(os.path.join(userprofile), 'Desktop')

        folder = os.path.join(os.path.join(desktop), 'CyberChef')
        if os.path.exists(folder):
            shutil.rmtree(folder)
        cyberchefFile = os.path.join(os.path.join(desktop), 'CyberChef.html')
        
        if os.path.islink(cyberchefFile):
            os.remove(cyberchefFile)