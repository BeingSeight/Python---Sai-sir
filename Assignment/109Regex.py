# 109. Regex Basics
import re

text = "Contact us at info@example.com or support@domain.org."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Emails found:", emails)