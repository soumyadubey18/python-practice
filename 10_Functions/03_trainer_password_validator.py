def password_validator(pwd):
    upper_count = 0
    lower_count = 0
    special_count = 0
    space_count = 0

    if len(pwd) < 8:
        return False

    for char in pwd:
        if char.isupper():
            upper_count += 1
        if char.islower():
            lower_count += 1
        if not char.isalnum() and not char.isspace():
            special_count += 1
        if char.isspace():
            space_count += 1

    return (
        lower_count >= 1
        and upper_count >= 1
        and special_count >= 1
        and space_count == 0
    )

tests = ["Soumya@123", "Soumya123", "Kumar#1", "GoodPass@2026"]

for pwd in tests:
    print(pwd, "=>", "Valid" if password_validator(pwd) else "Invalid")
