#from selenium import webdriver
from Google.Googlemain import GoogleExperienced,GoogleNew_Grad,GoogleInternship

def GoogleCareer(text):
    if(text=="Experienced"): 
        GoogleExperienced()
    if(text=="New_Grad"):
        GoogleNew_Grad()
    if(text=="Internship"):
        GoogleInternship()
        