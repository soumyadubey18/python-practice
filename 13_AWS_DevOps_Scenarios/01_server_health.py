def check_server(name, status, cpu):
    if status == "running" and cpu < 80:
        return f"{name}: HEALTHY"
    elif status != "running":
        return f"{name}: SERVER NOT RUNNING"
    else:
        return f"{name}: HIGH CPU"

servers = [
    ("web01", "running", 55),
    ("web02", "running", 91),
    ("web03", "stopped", 20),
]

for server in servers:
    print(check_server(*server))
