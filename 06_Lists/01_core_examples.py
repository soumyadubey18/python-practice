# Example 1: create/access
servers = ["web01", "web02", "web03"]
print(servers[0])
print(servers[-1])

# Example 2: modify
servers.append("web04")
servers[1] = "app01"
print(servers)

# Example 3: remove
servers.remove("web03")
last = servers.pop()
print(servers)
print("Removed:", last)

# Example 4: methods
numbers = [5, 2, 8, 2, 10]
numbers.sort()
print(numbers)
print("Count of 2:", numbers.count(2))
print("Length:", len(numbers))
