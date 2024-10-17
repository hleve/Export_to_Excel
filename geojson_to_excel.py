import json
import csv

# Replace the path with the path to your GeoJSON file
geojson_file_path = "path/to/your/geojson_file.geojson"
csv_file_path = "path/to/your/output_file.csv"

# Open and read the GeoJSON file
with open(geojson_file_path, "r", encoding="utf-8") as geojson_file:
    geojson_data = json.load(geojson_file)

# Extract the features from the GeoJSON data
features = geojson_data["features"]

# Extract the field names from the properties of the first feature
fieldnames = features[0]["properties"].keys()

# Write the data to a CSV file
with open(csv_file_path, "w", encoding="utf-8", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for feature in features:
        writer.writerow(feature["properties"])