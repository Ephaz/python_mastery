"""
def func_a(parameter/argument):
    y = x + 1
    return y
    
Defining a function"""

def g(y):
    print(f"inside a function g(y) {x}")
    print(f"inside a function g(y) {x + 1}")
    
x = 5
g(x)
print(f"outside a function {x}")

def f(y):
    x = 1
    x += 1
    print(x)
    return x

x = 5
d = f(x)
print(d)
print(x)