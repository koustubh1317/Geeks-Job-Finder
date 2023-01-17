#from selenium import webdriver
from Amazon.Amazonmain import AmazonExperienced,AmazonNew_Grad,AmazonInternship

def AmazonCareer(text):
    if(text=="Experienced"): 
        AmazonExperienced()
    if(text=="New_Grad"):
        AmazonNew_Grad()
    if(text=="Internship"):
        AmazonInternship()
        