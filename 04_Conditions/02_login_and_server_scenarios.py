# Login validation
username = "Mahesh"
password = "12345"

user = input("Username: ")
pwd = input("Password: ")

if username == user and password == pwd:
    print("Login successful")
elif username == user or password == pwd:
    if username == user and password != pwd:
        print("Correct username, incorrect password")
    elif username != user and password == pwd:
        print("Correct password, incorrect username")
else:
    print("Invalid credentials")

# AWS-style CPU alert
cpu = int(input("CPU usage: "))

if cpu >= 90:
    print("CRITICAL")
elif cpu >= 70:
    print("WARNING")
else:
    print("NORMAL")
