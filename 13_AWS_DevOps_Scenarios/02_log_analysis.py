logs = [
    "INFO server started",
    "ERROR database connection failed",
    "INFO request completed",
    "ERROR timeout",
    "INFO backup completed",
]

error_count = 0

for line in logs:
    if "ERROR" in line:
        error_count += 1
        print("Alert:", line)

print("Total errors:", error_count)
