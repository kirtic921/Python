# Fruit Ripeness Checker
# Determine whether fruit is ripe, unripe or overripe based on it's color - Banana

color = input("Enter the color of your banana: ")

if(color=='green'):
    print("Banana is unripe")
elif(color=='yellow'):
    print("Banana is ripe")
elif(color=='brown'):
    print("Banana is overripe")
else:
    print("Please enter a valid color of the banana")