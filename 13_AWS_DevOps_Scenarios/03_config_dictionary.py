config = {
    "region": "ap-south-1",
    "environment": "dev",
    "instance_type": "t3.micro",
    "monitoring": True,
}

for key, value in config.items():
    print(f"{key}: {value}")

if config["monitoring"]:
    print("Monitoring enabled")
