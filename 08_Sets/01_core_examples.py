# Example 1: remove duplicates
numbers = [1, 2, 2, 3, 3, 4]
unique = set(numbers)
print(unique)

# Example 2: add/remove
servers = {"web01", "web02"}
servers.add("web03")
servers.remove("web01")
print(servers)

# Example 3: mathematical operations
a = {"EC2", "S3", "RDS"}
b = {"S3", "RDS", "Lambda"}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric difference:", a ^ b)

# Example 4: membership
print("S3" in a)
