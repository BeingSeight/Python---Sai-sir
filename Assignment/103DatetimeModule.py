# 103. Use Datetime Module
from datetime import datetime

current_time = datetime.now()
print("Current time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))