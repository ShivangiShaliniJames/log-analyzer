import os
from analyzer import count_log_levels

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(BASE_DIR, "logs")
file_path = os.path.join(log_dir, "app.log")

if not os.path.exists(file_path):
    raise FileNotFoundError("Log file not found. Ensure logs/app.log exists.")

with open(file_path, "r") as file:
    logs = file.readlines()

result = count_log_levels(logs)

for level, count in result.items():
    print(f"{level}: {count}")

