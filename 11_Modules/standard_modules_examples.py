import os
import random
import datetime
import json

print("Current folder:", os.getcwd())
print("Random number:", random.randint(1, 10))
print("Today:", datetime.date.today())

server = {"name": "web01", "status": "running"}
json_text = json.dumps(server)
print(json_text)
