# Scenario 1: server is healthy only when running AND CPU is below 80
running = True
cpu = 65

if running and cpu < 80:
    print("Server is healthy")
else:
    print("Check server")

# Scenario 2: allow deployment if user is admin OR DevOps engineer
role = "DevOps"

if role == "admin" or role == "DevOps":
    print("Deployment allowed")
else:
    print("Deployment denied")

# Scenario 3: maintenance flag
maintenance = False
print("Traffic allowed:", not maintenance)

# Scenario 4: credentials
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
