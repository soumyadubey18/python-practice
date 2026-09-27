# Example 1: immutable string
name = "Soumya"
old_id = id(name)
name = name + " Dubey"
print(name)
print("ID changed:", old_id != id(name))

# Example 2: mutable list
servers = ["web01", "web02"]
old_id = id(servers)
servers.append("web03")
print(servers)
print("ID stayed same:", old_id == id(servers))

# Example 3: input() always returns str
name = input("Enter your name: ")
print(name, type(name))

# Example 4: numeric input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# print sep and end
print("AWS", "EC2", "S3", sep=" | ")
print("Hello", end=" ")
print("Soumya")
