# AWS-style nested dictionary (practice representation)
instance = {
    "id": "i-12345",
    "state": {"name": "running"},
    "tags": {"Name": "web-server", "Environment": "dev"},
    "region": "ap-south-1"
}

print(instance["id"])
print(instance["state"]["name"])
print(instance["tags"]["Name"])

# Filter server records
servers = [
    {"name": "web01", "status": "running"},
    {"name": "web02", "status": "stopped"},
    {"name": "web03", "status": "running"},
]

for server in servers:
    if server["status"] == "running":
        print(server["name"], "is running")

# Merge dictionaries
base = {"environment": "dev", "owner": "Soumya"}
extra = {"region": "ap-south-1", "project": "python"}
merged = {**base, **extra}
print(merged)
