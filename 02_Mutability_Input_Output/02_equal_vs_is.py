# == compares value/content
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True

# is compares identity/object
print(a is b)  # False

# Best practice: use is for None
value = None
print(value is None)
