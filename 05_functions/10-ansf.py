# Recursive function
# Problem: Create a recursive function that will calculate the factorial of a number.

def fact(n):
    if(n!=1):
        return n*fact(n-1)
    elif(n==1):
        return 1

print(fact(5))
            