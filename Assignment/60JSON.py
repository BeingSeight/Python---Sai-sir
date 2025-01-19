# 60. JSON Read & Write
import json
file_name = input("Enter the JSON file name: ")
try:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
    print("Original data:", data)
    key_to_modify = input("Enter the key to modify: ")
    new_value = input("Enter the new value: ")
    data[key_to_modify] = new_value
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Data updated successfully.")
except FileNotFoundError:
    print("JSON file not found.")