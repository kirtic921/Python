# Factorial Calculator
# Problem: Compute the factorial of a number using while loop.

number=input("Enter a number: ")
inumber=int(number)
i=1
fact=1

while(i<=inumber):
    fact*=i
    i+=1

print("Factorial of entered value is", fact)