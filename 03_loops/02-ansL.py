# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n=input("Enter a number: ")
i_n=int(n)
sum = 0

series = range(0,i_n+1)

for i in series:
    sum = sum + i

statement = "Sum of all the even numbers uptil {} is {}"
print(statement.format(n, sum))
