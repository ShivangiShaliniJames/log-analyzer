import os
from analyzer import count_log_levels

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "logs", "app.log")

with open(file_path, "r") as file:
    logs = file.readlines()

result = count_log_levels(logs)

print("Log Summary:")
for level, count in result.items():
    print(f"{level}: {count}")
