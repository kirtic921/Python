# 2. Movie Ticket Pricing
# Problem: Movie Tickets are priced based on age: $12 for adults(18 and over), $8 for children. Everyone gets a discount on Wednesday.

age=input("Enter your age: ")
iage=int(age)
day=input("Enter the day:")

if(iage<18 and day!='Wednesday'):{
    print("Ticket price is $8.")
}
elif(iage<18 and day=='Wednesday'):{
    print("Ticket price is $6.")
}
elif(iage>=18 and day=='Wednesday'):{
    print("Ticket price is $10.")
}
else:{
    print("Ticket price is $12.")
}