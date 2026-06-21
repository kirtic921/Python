# Default parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with the default name.

# messed-up
# def greet(name):
#     if not name:
#         print("Hi","user",". How's the day going?")
#     else:
#         print("Hi",name,". How's the day going?")

# greet("Kirti")

# WORKING METHOD

def greet(name="User"):
    return "Hi "+name+"!"

print(greet("Kirti"))
print(greet())