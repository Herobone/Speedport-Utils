from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import sys
import time
from influx import InfluxDB
import json
import argparse

# Url of the speedport
# Could also be an ip (192.168.136.1)
url = "http://speedport.ip/"

# generate filename of the geckodriver
geckoName = "geckodriver.exe" if sys.platform == "win32" else "geckodriver"

# Get absolut path of geckodriver
geckoPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), geckoName)

# Get absolut path of config file
configFile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "r")
config = json.load(configFile)  # Load the json config file to a dict
configFile.close()

# Load important values from config
host = config.get('host')
port = config.get('port')
database = config.get('database')
waitTime = config.get('interval')

client = None

def readVars(verboose=False):
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=geckoPath)
    driver.get(url)

    # go to the status page
    statusMenu = driver.find_element_by_id("navStatus")
    while not statusMenu.is_displayed():
        pass
    statusMenu.find_element_by_tag_name("a").click()

    # get the download speed element
    downSpeedElement = driver.find_element_by_id(id_='var_inet_download')
    while not downSpeedElement.is_displayed():
        pass

    # get the upload speed element
    upSpeedElement = driver.find_element_by_id(id_='var_inet_upload')
    while not upSpeedElement.is_displayed():
        pass

    # Parse the element values to variables
    down = int(downSpeedElement.text)
    up = int(upSpeedElement.text)
    driver.quit()

    return up, down

def postVars(up, down):
    # Construct the connection to InfluxDB
    client = InfluxDB('http://' + host + ':' + str(port))
    # Post data to db
    client.write(database, 'DSLDownRate', fields={'value': down})
    client.write(database, 'DSLUpRate', fields={'value': up})

def jsonDumpVars(up, down):
    print("ERROR: Not implemented jet")

def txtDumpVars(up, down):
    print("ERROR: Not implemented jet")

def processVars(up, down, action="DB", verboose = False):
    if action.lower() == "DB".lower():
        postVars(up, down)

    elif action.lower() == "JSON".lower():
        jsonDumpVars(up, down)

    elif action.lower() == "TXT".lower():
        txtDumpVars(up, down)

    elif action.lower() == "LOG".lower():
        print("Upload:", up)
        print("Download:", down)

    if (verboose):
        print("Download:", down)
        print("Upload:", up)

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type", required=False, default="multi",
        help="Set the type of execution (multi/single)")
    ap.add_argument("-a", "--action", required=False, default="DB",
        help="Set the action it should do (DB/JSON/TXT/LOG)")
    ap.add_argument("-q", "--quiet", required=False, help="No output", action='store_true')
    ap.add_argument("-v", "--verboose", required=False, help="Output debug/information messages", action='store_true')
    args = ap.parse_args()

    # Print Debug messages if program is not quiet
    if not args.quiet:
        print("Process started!")
        if args.action.lower() == "DB".lower():
            print("Sending measurements to InfluxDB")
            print("Host: ", host)
            print("Port: ", port)
            print("Database: ", database)

        elif args.action.lower() == "JSON".lower():
            print("Printing to JSON")

        elif args.action.lower() == "TXT".lower():
            print("Printing to TXT")

        elif args.action.lower() == "LOG".lower():
            print("Printing to LOG")

        print("Geckodriver found: ", os.path.isfile(geckoPath))
        print("Geckodriver path: ", geckoPath)
        if(args.type == "multi"):
            print("Interval: {} seconds".format(waitTime))

    # only continue if the geckodriver was found
    if not os.path.isfile(geckoPath):
        return -1

    # if the type is multi it will continue processing
    while (args.type == "multi"):
        up, down = readVars(verboose=args.verboose)
        processVars(up, down, action=args.action, verboose=args.verboose)
        time.sleep(waitTime)
    
    # if the type is single it only processes once
    if (args.type == "single"):
        up, down = readVars(verboose=args.verboose)
        processVars(up, down, action=args.action, verboose=args.verboose)

if __name__ == '__main__':
    main()