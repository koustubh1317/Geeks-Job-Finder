import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#list of xpaths
amazon_student_job_button='//*[@id="homepage"]/div[3]/div/div/div[1]/div/div/div[2]/a'
amazon_experienced_job_button='//*[@id="homepage"]/div[3]/div/div/div[3]/div/div/div[2]/a'
amazon_job_filter_experienced='//*[@id="desktopFilter_job_type_filter"]/div/div/fieldset/div/button[1]/div'
amazon_job_expand='//*[@id="search-results-box"]/div[2]/div/div/div[2]/content/div/div/div[2]/div[2]/div/div[1]/a/div/div[1]/div[1]/h3'
amazon_job_filter_internship='//*[@id="desktopFilter_job_type_filter"]/div/div/fieldset/div/button[3]/div/span'
amazon_job_filter_newgrad='//*[@id="desktopFilter_job_type_filter"]/div/div/fieldset/div/button[1]/div/span'


def AmazonExperienced():
    driver=webdriver.Chrome()
    driver.get('https://www.amazon.jobs/en/')
    wait=WebDriverWait(driver,10)
     
    wait.until(EC.element_to_be_clickable((By.XPATH,amazon_experienced_job_button))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,amazon_job_filter_experienced))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,amazon_job_expand))).click()
     
    get_url = driver.current_url
    print("The current url is:"+str(get_url))

    time.sleep(10)

def AmazonNew_Grad():
    driver=webdriver.Chrome()
    driver.get('https://www.amazon.jobs/en/')
    driver.find_element('xpath',amazon_student_job_button).click()
    time.sleep(4)
    driver.find_element('xpath',amazon_job_filter_newgrad).click()
    time.sleep(4)
    driver.find_element('xpath',amazon_job_expand).click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))

    time.sleep(10)


def AmazonInternship():
    driver=webdriver.Chrome()
    driver.get('https://www.amazon.jobs/en/')
    driver.find_element('xpath',amazon_student_job_button).click()
    time.sleep(4)
    driver.find_element('xpath',amazon_job_filter_internship).click()
    time.sleep(4)
    driver.find_element('xpath',amazon_job_expand).click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))
   
    time.sleep(10)