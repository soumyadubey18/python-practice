# Validation methods
value = "AWS123"
print(value.isalnum())
print(value.isalpha())
print("123".isdigit())
print("Hello".isalpha())

# Count characters
text = "automation"
print("a count:", text.count("a"))

# Palindrome
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Password validator - trainer-style logic
password = "Soumya@123"
upper = lower = special = spaces = 0

for char in password:
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
    if not char.isalnum() and not char.isspace():
        special += 1
    if char.isspace():
        spaces += 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and special >= 1 and spaces == 0:
    print("Valid password")
else:
    print("Invalid password")
