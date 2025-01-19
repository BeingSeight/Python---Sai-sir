# 85. CSV Reader
import csv
def read_csv(file_path: str):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("CSV file not found.")
read_csv("example.csv")
