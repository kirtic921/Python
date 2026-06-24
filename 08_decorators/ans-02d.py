# Debugging Function Calls 
# Create a decorator to print the function name and the values of its arguments every time the function is called.

def toll_function(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        print(f"Function name is: {func.__name__} & arguments passed are: {args}")
        return result
    return wrapper

@toll_function
def main_function(a,b):
    print("Sum of parameters entered is: ", a+b)

main_function(5,3)

# MINE SOUTION