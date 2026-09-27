# Nested list
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0][1])

# List comprehension: squares
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# Filter even values
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

# AWS-style server names
servers = ["web01", "db01", "web02", "cache01"]
web_servers = [s for s in servers if s.startswith("web")]
print(web_servers)
