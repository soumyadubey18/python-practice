# Example 1: greatest of two
num1 = 200
num2 = 100

if num1 > num2:
    print(num1)
else:
    print(num2)

# Example 2: travel decision
balance = 4200
if balance >= 5000:
    print("Kerala")
elif balance > 4000:
    print("Mangalore")
else:
    print("Stay home")

# Example 3: percentage decision
percentage = 95
if percentage > 90:
    print("Science")
elif percentage > 70:
    print("Commerce")
else:
    print("Arts")

# Example 4: nested condition
percentage = 96
if percentage > 90:
    if percentage > 97:
        print("PCMB")
    elif percentage > 94:
        print("PCMC")
    else:
        print("PCME")
