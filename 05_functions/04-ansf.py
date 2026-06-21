# Functions Returning Multiple Values
# Problem: Create a function that returns both the circumference and area of  a circle.

def circle(radius):
    area=float(3.14)*float(radius)*float(radius)
    circumference=float(3.14)*float(2)*float(radius)
    return area,circumference

a,c=circle(8)
print("Area:",a," ;Circumference:",c)