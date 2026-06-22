# Generator Function with yield
# Problem: Write a generator function that will generate even numbers upto a specified limit. 

def generate_even(number):
    for i in range(0, number+1):
        if(i%2==0):
            print(i)

# def even(n):
#     for i in range(2, n+1, 2):
#         return i
# print(even(23))  

generate_even(23)