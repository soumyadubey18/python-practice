# Example 1: create/access
server = {"name": "web01", "status": "running", "cpu": 65}
print(server["name"])
print(server["status"])

# Example 2: update/add
server["cpu"] = 85
server["region"] = "ap-south-1"
print(server)

# Example 3: methods
print(server.keys())
print(server.values())
print(server.items())

# Example 4: loop
for key, value in server.items():
    print(key, "=>", value)
