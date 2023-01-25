import sys
print(sys.version)
from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
from lxml import etree
import requests
  
  
URL = "https://careers.google.com/jobs/results/87562051456508614-software-engineering-manager-ii-google-cloud/"
  
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get(URL)
page = driver.execute_script('return document.body.innerHTML')
soup=BeautifulSoup(''.join(page), 'html.parser')
print(soup)
file1 = open("myfile.txt","w+")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(soup.text)

#r= urllib.request.urlopen('').read()
#soup=BeautifulSoup(r, "lxml")
#type(soup)
#print(soup.prettify()[:1000])
#for link in soup.find_all('a'):
#   print(link.get('href'))
#print(soup.get_text())
