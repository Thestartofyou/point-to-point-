import pandas as pd
from geopy.distance import geodesic

# Load the Excel file containing area data
excel_file = 'areas.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Assuming your Excel file has columns 'Area', 'Latitude', and 'Longitude'
# You may need to adjust these column names based on your Excel file structure

# Create a dictionary to store coordinates for each area
coordinates = {}

for index, row in df.iterrows():
    area = row['Area']
    latitude = row['Latitude']
    longitude = row['Longitude']
    coordinates[area] = (latitude, longitude)

# Calculate distances between different areas
def calculate_distance(area1, area2):
    if area1 in coordinates and area2 in coordinates:
        coord1 = coordinates[area1]
        coord2 = coordinates[area2]
        distance = geodesic(coord1, coord2).kilometers
        return distance
    else:
        return None  # Return None if coordinates are not found

# Example usage
area1 = 'Area1'  # Replace with the name of the first area
area2 = 'Area2'  # Replace with the name of the second area

distance = calculate_distance(area1, area2)

if distance is not None:
    print(f"Distance between {area1} and {area2}: {distance:.2f} kilometers")
else:
    print(f"Coordinates not found for one or both of the areas.")
