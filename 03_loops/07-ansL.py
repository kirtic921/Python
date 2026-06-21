# Validate input
# Problem: Keep asking the user for input until they enter a number between 1 and 10

i=input("Enter a number: ")
int_i=int(i)

while(int_i<1 or int_i>10):
    i=input("Enter a number: ")
    int_i=int(i)
    if(int_i>=1 and int_i<=10):
        break
        
print("You just entered number in my domain:", int_i)

