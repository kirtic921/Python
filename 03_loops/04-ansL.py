# Reverse a String
# Problem: Reverse a string using loop.

str=input("Enter a string: ")
print(str)
n=len(str)
series= range(0, n)
output=''

for i in series:
    output+=str[n-i-1]


print("The reversed string :", output)

