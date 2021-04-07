# -*- coding: utf-8 -*-

print '''
Python Selenium Safari Example
'''

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import os
import re

# path to selenium server standalone jar, downloaded here:
# http://docs.seleniumhq.org/download/
# or a direct url:
# http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar
os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
# note: I've put this jar file in the same folder as this python file

browser = webdriver.Safari()

# makes the browser wait if it can't find an element
browser.implicitly_wait(10)

browser.get("https://downdetector.com.br/fora-do-ar/whatsapp/")

# dataScript = browser.find_elements_by_id("holder")

# dataScript = browser.find_elements_by_id("overlay")
dataScript = browser.find_element_by_xpath("//*[@id='chart-row']/div/div/script[1]").get_attribute('innerHTML')


pattern = re.compile(r"data: \[[\s]+\{[\sa-z\:\'0-9\-\+\.\,\}\{]+\]", re.I)

pattern.search(dataScript)
valueReturn = pattern.findall(dataScript)[0]

f = open("data.txt","w")
f.write(valueReturn)
f.close()

browser.quit()