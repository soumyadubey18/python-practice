# Positional
def power(base, exponent):
    return base ** exponent

print(power(2, 3))

# Keyword
print(power(exponent=3, base=2))

# *args
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))

# **kwargs
def show_server(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_server(name="web01", status="running", region="ap-south-1")

# Lambda
square = lambda x: x ** 2
print(square(5))

# map + lambda
numbers = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, numbers)))

# Recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
