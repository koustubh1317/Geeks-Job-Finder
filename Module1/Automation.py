from Google.option import GoogleCareer
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
    print("Success")
    
main()
    