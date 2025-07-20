import pandas as pd

# Define file path
file_path = "usa-housing-data-county-2017-cleaned.csv"

# Load only the GEONAME column
df = pd.read_csv(file_path, usecols=["GEONAME"])

# Get unique values
unique_geonames = df["GEONAME"].dropna().unique()

# Save to a text file
with open("unique_geonames.txt", "w") as f:
    for geoname in unique_geonames:
        f.write(geoname + "\n")

print(f"Unique GEONAME values saved to unique_geonames.txt")

