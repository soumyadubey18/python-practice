# Example 1: indexing and slicing
text = "Python"
print(text[0])
print(text[-1])
print(text[0:3])
print(text[::-1])

# Example 2: case methods
name = "soumya dubey"
print(name.upper())
print(name.lower())
print(name.title())

# Example 3: split, join, strip
raw = "  web01,web02,web03  "
items = raw.strip().split(",")
print(items)
print(" | ".join(items))

# Example 4: find/replace
message = "server is down"
print(message.find("down"))
print(message.replace("down", "up"))
