import csv
import json

# Replace the path with the path to your JSON file
with open("filepath", "r", encoding="utf-8") as f:
    input_file = json.load(f)

# Extract the field names from the first dictionary
fieldnames = [field['name'] for field in input_file[0]['data']['fields']]

# Write the data to a CSV file
# Replace the path with the path to your CSV file
with open("filepath", "w", encoding="utf-8", newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(fieldnames)
    for d in input_file:
        for row in d["data"]["rows"]:
            writer.writerow(row)
