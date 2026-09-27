# 1. Sum 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# 2. Multiplication table
num = 7
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 3. Count running servers
servers = ["running", "stopped", "running", "running", "stopped"]
count = 0
for status in servers:
    if status == "running":
        count += 1
print("Running servers:", count)

# 4. Find first failed check
checks = ["OK", "OK", "OK", "FAIL", "OK"]
for check in checks:
    if check == "FAIL":
        print("Failure detected")
        break
