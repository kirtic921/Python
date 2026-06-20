# Grade Calculator
# Assign grade according to score: A(90-100), B(80-89), C(70-79), D(60-69), E(50-59), F(<50)

score = input("Enter your marks:")
iscore= int(score)


if(iscore>=101):
    print("Please check your score you just entered!")
    exit()

if(iscore>=90):
    grade='A'
elif(iscore>=80 and iscore<=89):
    grade='B' 
elif(iscore>=70 and iscore<=79):
    grade='C' 
elif(iscore>=60 and iscore<=69):
    grade='D'
elif(iscore>=50 and iscore<=59):
    grade='E'
else:
    grade='Fail'

print("Your Grade: ", grade)  