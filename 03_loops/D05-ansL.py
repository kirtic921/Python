# Find the first non repeated character
# Problem: Given a string, find the first non-repeated character.

str=input("Enter a string: ")
n=len(str)

# messed-up
# for i in range(0, n):
#     curr=str[i]
#     for int in range(0, n):
#         if(i!=int):
#             if(curr!=str[int]):
#                 output=curr
#             else:
#                 output=""
#                 exit()

# print(output)

# WORKING METHOD
for char in str:
    if str.count(char)==1:
        print("First non-repeated char is",char)
        break