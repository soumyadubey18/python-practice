# Example 1: without return
def greet(name):
    print(f"Hello {name}")

greet("Soumya")

# Example 2: with return
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Example 3: default argument
def welcome(name, course="Python"):
    print(f"{name} is learning {course}")

welcome("Soumya")
welcome("Soumya", "AWS")

# Example 4: practical function
def is_healthy(cpu):
    return cpu < 80

print(is_healthy(65))
print(is_healthy(90))
