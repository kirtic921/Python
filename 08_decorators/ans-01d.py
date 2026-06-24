# Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result = func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time.")
        return result
    return wrapper

@timer
def eg_func(n):
    time.sleep(n)

eg_func(4)