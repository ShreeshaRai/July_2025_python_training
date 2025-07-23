
from datetime import datetime
dob_input=input("enter date in formate [dd-mm-yyyy]")
dob=datetime.strptime(dob_input,"%d-%m-%y")
today=datetime.today()
age=today.year()-dob.year()
if(today.month,today.day)<(dob.month,dob.day):
    age=age-1
print(age)


