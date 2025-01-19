
# 55. CSV Reader
import csv
file_name = input("Enter the CSV file name: ")
try:
    with open(file_name, newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
