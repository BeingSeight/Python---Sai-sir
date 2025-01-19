# 108. Requests Module
import requests

response = requests.get("https://api.publicapis.org/entries")
if response.status_code == 200:
    data = response.json()
    print("API Description:", data["entries"][0]["Description"])