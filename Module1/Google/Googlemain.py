import time
from selenium import webdriver

#list of xpaths
google_job_button="/html/body/div[1]/header/div[1]/div[1]/nav/ul/li[4]/a"
google_job_type_button='//*[@id="jump-content"]/div[1]/div/div[1]/div/div/div/div[3]/div[6]'
google_job_filter_experienced='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[1]/label/span'
google_job_expand='//*[@id="search-results"]/li[1]/a/div/div[1]/h2'
google_job_filter_internship='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[4]/label/span'
google_job_filter1_newgrad='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[2]/label/span'
google_job_filter2_newgrad='//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[3]/label/span'


def GoogleExperienced():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
     
    driver.find_element('xpath',google_job_button).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_type_button).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_filter_experienced).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_expand).click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    driver.close()
    time.sleep(10)

def GoogleNew_Grad():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    driver.find_element('xpath',google_job_button).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_type_button).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_filter_experienced).click()
    time.sleep(1)
    driver.find_element('xpath',google_job_filter1_newgrad).click()
    time.sleep(1)
    driver.find_element('xpath',google_job_filter2_newgrad).click()
    time.sleep(1)
    driver.find_element('xpath',google_job_expand).click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    driver.close()
    time.sleep(10)


def GoogleInternship():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    driver.find_element('xpath',google_job_button).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_type_button).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_filter_internship).click()
    time.sleep(4)
    driver.find_element('xpath',google_job_expand).click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    driver.close()
    time.sleep(10)