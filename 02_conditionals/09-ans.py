# Leap year Checker
# Problem: Determine if a year is a leap year.(Leap years are divisible by 4, but not by 100 until also divisible by 400)

year=input("Enter the year: ")
iyear=int(year)

if(iyear%400==0):
    status=' a Leap Year'
elif(iyear%4==0 and iyear%100!=0):
    status='Leap year'
else:
    status='Not a leap year'

print("The year you just entered is", status)