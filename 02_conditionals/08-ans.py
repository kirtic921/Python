# Password Strength Checker
# Problem: Check if a passsword is "Weak", "Medium", "Strong" (Criteria - <6chars:weak ; 6-10chars: medium ; >10chars: stong)

password = input("Enter your password: ")
size=len(password)

if(size<6):
    status="Weak"
elif(size>=6 and size<=10):
    status="Medium"
elif(size>10):
    status="Strong"

print("The status of your password is", status)
