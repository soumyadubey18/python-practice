# Example 1: range
for i in range(1, 6):
    print(i)

# Example 2: even numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Example 3: while
count = 1
while count <= 5:
    print("Attempt", count)
    count += 1

# Example 4: break and continue
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print("continue example:", i)
