# 1. Arithmetic
a, b = 20, 6
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** 2)

# 2. Comparison
cpu = 85
print(cpu > 80)
print(cpu == 85)
print(cpu != 50)

# 3. Logical
server_running = True
cpu_high = True
print(server_running and cpu_high)
print(server_running or cpu_high)
print(not server_running)

# 4. Membership + identity
name = "Python"
print("P" in name)
x = None
print(x is None)

# 5. Swap
a, b = "EC2", "S3"
a, b = b, a
print(a, b)
