# Multiplication Table Printer
# Problem: Print the multiplication table for a given nuumber up to 10, but skip the fifth iteration.

n = input("Enter a number: ")
i_n = int(n)

series = range(0, 11)

print("The Multiplication table for the entered value (skipping the fifth iteration) is as follows: \n")

# Method-1
# for i in series:
#     if(i!=5):
#         print(i_n*i)

# Method 2
for i in series:
    if(i==5):
        continue
        
    print(i_n,'X', i, '=', i_n*i)    

    