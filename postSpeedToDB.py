from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import sys
import time
from influx import InfluxDB
import json

url = "http://speedport.ip/"

fname = "geckodriver.exe" if sys.platform == "win32" else "geckodriver"

filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),fname)

configFile = open("config.json", "r")
config = json.load(configFile)
configFile.close()

host = config.get('host')
port = config.get('port')

database = config.get('database')

client = InfluxDB('http://' + host + ':' + str(port))

waitTime = config.get('interval')

def postUpDown():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=filePath)
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

    client.write(database, 'DSLDownRate', fields={'value': int(downSpeedElement.text)})
    client.write(database, 'DSLUpRate', fields={'value': int(upSpeedElement.text)})
    driver.quit()

def main():
    print("Process started!")
    print("Host: ", host)
    print("Port: ", port)
    print("Database: ", database)
    print("Geckodriver found: ", os.path.isfile(filePath))
    print("Geckodriver path: ", filePath)
    print("Interval: {} seconds".format(waitTime))
    if not os.path.isfile(filePath):
        return -1
    while (True):
        postUpDown()
        time.sleep(waitTime)

if __name__ == '__main__':
    main()
