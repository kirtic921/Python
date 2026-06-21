# Prime number checker
# Problem: Check if a number is prime
n=input("Enter a number: ")
number=int(n)

if(number<=1):
    status='NOT a prime number.'
# elif(number==2):
#     status='a prime number'
elif(number>1):
    series=range(2,number)
    for i in series:
        if(number%i!=0):
            status='a prime number'
        else:
            status='NOT a prime number'
            break

print("The number you entered:", status)
# METHOD 2, (can't check negative numbers with below logic)
# number = -1

# is_prime=True

# if number>1:
#     for i in range(2, number):
#         is_prime=False
#         break

# print("Is prime-", is_prime)

