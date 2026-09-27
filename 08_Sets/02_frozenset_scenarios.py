# frozenset is immutable
allowed_regions = frozenset({"ap-south-1", "us-east-1"})
print(allowed_regions)
print("ap-south-1" in allowed_regions)

# Compare two teams' skills
team_a = {"Linux", "AWS", "Git"}
team_b = {"AWS", "Python", "Git"}
print("Common:", team_a & team_b)
print("Only team A:", team_a - team_b)

# Duplicate log events
events = ["login", "login", "deploy", "login", "deploy"]
print(set(events))

# Unique AWS services
services = ["EC2", "S3", "EC2", "IAM", "S3"]
print(set(services))
