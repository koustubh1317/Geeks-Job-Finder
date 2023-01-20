from Google.option import GoogleCareer
from Amazon.option import AmazonCareer

def main():
    print("WELCOME TO GEEKS JOB FINDER")
    print("PLEASE SELECT YOUR CATEGORY")   
    
    print("1.Experienced") 
    print("2.New Grad")
    print("3.Internship")
    val=int(input())
    text=""
    
    if(val==1):
       text="Experienced"
    if(val==2):
       text="New_Grad"
    if(val==3):
       text="Internship"
    
    GoogleCareer(text)
    AmazonCareer(text)
    print("Success")
    
main()
    