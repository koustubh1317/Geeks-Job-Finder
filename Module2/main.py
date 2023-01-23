import sys
print(sys.version)
from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
from lxml import etree
import requests
  
  
URL = "https://careers.microsoft.com/us/en/job/1514705/Senior-Product-Manager-CTJ-Poly"
  
response=requests.get(URL)
soup=BeautifulSoup(response.text,'lxml')
print(soup)
N=soup.find_all('div',class_='job-other-info')
print(N)
dom=etree.HTML(str(soup))
res=(dom.xpath('//*[@id="coreui-featuregroup-ydkoz9c"]/div/div[1]/h1'))
print(res)


#r= urllib.request.urlopen('').read()
#soup=BeautifulSoup(r, "lxml")
#type(soup)
#print(soup.prettify()[:1000])
#for link in soup.find_all('a'):
#   print(link.get('href'))
#print(soup.get_text())
