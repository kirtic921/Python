# 1. Age group categorization
# Problem- Classify a person's group age: Child(<13), Teenager(<20), Adult(<60), Senior(>=60)

age = input ("Enter your age: \n")
age_int = int (age)

if(age_int<=13):{
    print("Child")}
elif(age_int<=19):
    print("Teenager")
elif(age_int<=59):
    print("Adult")
elif(age_int>=60):
    print("Senior")