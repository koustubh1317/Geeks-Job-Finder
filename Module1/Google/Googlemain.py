import time
from selenium import webdriver

#list of xpaths


def GoogleExperienced():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    google_job_button=driver.find_element('xpath','/html/body/div[1]/header/div[1]/div[1]/nav/ul/li[4]/a')
    google_job_button.click()
    #print(google_job_button)
    time.sleep(4)
    google_job_type_select=driver.find_element('xpath','//*[@id="jump-content"]/div[1]/div/div[1]/div/div/div/div[3]/div[6]')
    google_job_type_select.click()
    #print(google_job_type_select)  
    time.sleep(4)
    google_job_type_full=driver.find_element('xpath','//*[@id="accordion-accordion-employment-type"]/div/fieldset/ul/li[1]/label/span')
    google_job_type_full.click()
    time.sleep(4)
    google_job_expand=driver.find_element('xpath','//*[@id="search-results"]/li[1]/a/div/div[1]/h2')
    google_job_expand.click()

    get_url = driver.current_url
    print("The current url is:"+str(get_url))
    driver.close()
    time.sleep(10)

def GoogleNew_Grad():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    print("HELLO NEW GRAD")
def GoogleInternship():
    driver=webdriver.Chrome()
    driver.get('https://careers.google.com/')
    print("INTERNSHIP")