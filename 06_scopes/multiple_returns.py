def f1(num):
    def actual(x):
        return x**num
    return actual

f=f1(2)
g=f1(3)

print(f(2))
print(g(2))