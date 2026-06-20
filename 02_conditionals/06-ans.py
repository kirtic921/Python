# Transportation Mode Selection
# Problem: Choose a mode of transport based on distance

distance = input("Enter distance (in km): ")
idist=int(distance)

if(idist<3):
    transport='Walk'
elif(idist>=3 or idist<=15):
    transport='Bike'
elif(idist>15):
    transport='Car'
else:
    print("Recheck, Enter valid distance.")

print(transport)

