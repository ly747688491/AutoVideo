from datetime import datetime

now = datetime.now()

before_time = "2023-08-20 15:18:16"

before = datetime.strptime(before_time, "%Y-%m-%d %H:%M:%S")

print(now.date())
print(before.date())
print(now.date() == before.date())