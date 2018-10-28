import requests
import zipfile
import io
import os
import sys
import platform
from tqdm import tqdm
import requests
import math
import tarfile

def install():
    versionUrl = "https://github.com/mozilla/geckodriver/releases/latest"
    fname = ""
    url = ""
    filePath = ""

    vr = requests.get(versionUrl)
    print(vr.url)
    versionUrlArray = str(vr.url).split("/")
    version = versionUrlArray[len(versionUrlArray) - 1]

    system = sys.platform.replace("32", "") + platform.architecture()[0].replace("bit", "")

    print("System: ", platform.architecture()[0])
    print("System: ", system)

    fileType = sys.platform.replace("win32", "zip").replace("linux", "tar.gz")

    fname = "geckodriver-" + version + "-" + system + "." + fileType
    url = "https://github.com/mozilla/geckodriver/releases/download/" + version + "/" + fname

    filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),fname)
    print("File path: ", filePath)

    print("Downloading ", url)
    if not os.path.isfile(filePath):
        # Streaming, so we can iterate over the response.
        r = requests.get(url, stream=True)

        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0)); 
        block_size = 1024
        wrote = 0 
        with open(fname, 'wb') as f:
            for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
                wrote = wrote  + len(data)
                f.write(data)
        if total_size != 0 and wrote != total_size:
            print("ERROR, something went wrong")

    print("Extracting File")

    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()
    elif (fname.endswith("tar")):
        tar = tarfile.open(fname, "r:")
        tar.extractall()
        tar.close()
    elif (fname.endswith("zip")):
        tar = zipfile.ZipFile(fname, "r")
        tar.extractall()
        tar.close()