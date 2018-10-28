from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import sys

url = "http://speedport.ip/"

fname = "geckodriver"

if sys.platform is "win32":
    fname = "geckodriver.exe"

filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),fname)
print("File path: ", filePath)

options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options, executable_path=filePath)
driver.get(url)
print ("Headless Firefox Initialized")

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

print(downSpeedElement.text)
print(upSpeedElement.text)
driver.quit()
