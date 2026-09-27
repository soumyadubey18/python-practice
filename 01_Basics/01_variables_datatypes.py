# Example 1: basic variables
name = "Soumya"
age = 31
course = "Python"
is_learning = True

print(name, age, course, is_learning)
print(type(name), type(age), type(course), type(is_learning))

# Example 2: dynamic typing
value = 100
print(value, type(value))
value = "100"
print(value, type(value))

# Example 3: AWS-style configuration
region = "ap-south-1"
instance_count = 3
cpu_usage = 72.5
server_running = True

print(f"Region: {region}")
print(f"Instances: {instance_count}")
print(f"CPU: {cpu_usage}%")
print(f"Running: {server_running}")

# Example 4: type conversion
port = "80"
port_number = int(port)
print(port_number + 1)
