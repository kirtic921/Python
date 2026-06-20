# Reverse a String
# Problem: Reverse a string using loop.

str=input("Enter a string: ")
# Method-1
# print(str)
# n=len(str)
# series= range(0, n)
# output=''

# for i in series:
#     output+=str[n-i-1]

# METHOD-2
output=''
for char in str:
    output=char+output

print("The reversed string :", output)

