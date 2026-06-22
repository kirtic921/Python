# Function with **kwargs
# Problem: Create a function that accepts any number of keywords and prints them in format key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Shaktiman", power="laser", enemy="Dr. Jackaal")