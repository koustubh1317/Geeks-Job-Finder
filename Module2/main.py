import time
import csv
from bs4 import BeautifulSoup
from IPython.display import HTML
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

google=[]
l=""
d=""
fieldnames = ['Company_Name','Job_title','url','location','description']
google_back='/html/body/div[1]/header/div[1]/div[2]/div/div/button'
URL = "https://careers.google.com/jobs/results/?distance=50&employment_type=INTERN"
  
from selenium import webdriver

def text_decode(txt):
    str=""
    for s in txt:
        if(s=='>'):
            t=1
        elif(s=='<'):
            t=0
        if(t==1 and s!='>'):
           str+=s
    return str
           
           

def job_scrape(index):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    wait=WebDriverWait(driver,30)
    while True:
        try:
          
            google_job_expand='//*[@id="search-results"]/li['+str(index)+']/div/a/div'
         
            wait.until(EC.element_to_be_clickable((By.XPATH,google_job_expand))).click()
            wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[1]/h1')))
            page = driver.execute_script('return document.body.innerHTML')
            soup=BeautifulSoup(''.join(page), 'html.parser')
            dom = etree.HTML(str(soup))
            index+=1 
            job_url=driver.current_url
        
            loca=dom.xpath('//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[1]/ul[2]/li[2]')

            desc=dom.xpath('//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[2]/div[2]')
            for article in loca:
                l=etree.tostring(article, pretty_print=True).decode()
                l=text_decode(l)
            for article1 in desc:
                d=etree.tostring(article1, pretty_print=True).decode()
            
            job_data={
                'Company_Name':'Google',
                'Job_title':dom.xpath('//*[@id="jump-content"]/main/div/div[2]/div/div/div/div[1]/div[1]/h1')[0].text,
                'url':job_url,
                'location':l,
                'description':text_decode(d)

            } 
            google.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,google_back))).click() 
            #time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results"]/li['+str(index-1)+']/div/a/div/div[1]/h2')))
            driver.execute_script("window.scrollTo(0, 1080)") 
            print("index")
        except TimeoutException:
            driver.quit()
            break
def add_to_csv(fieldnames,google):
    with open('Openings.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
            #writer.writeheader()
        writer.writerows(google)


job_scrape(1)
add_to_csv(fieldnames,google)
