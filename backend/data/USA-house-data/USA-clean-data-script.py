import pandas as pd

# Define file paths
input_file = "usa-housing-data-county.csv"  # Input dataset
output_file = "usa-housing-data-county-2017-cleaned.csv"  # Output dataset

# Load the dataset
df = pd.read_csv(input_file)

# Filter data where PURPOSE is "Both" and YEAR is 2017 or greater
filtered_df = df[(df["PURPOSE"] == "Both") & (df["YEAR"] >= 2017)]

# Save the cleaned dataset, overwriting if it exists
filtered_df.to_csv(output_file, index=False)

print(f"Filtered dataset saved as {output_file} with {len(filtered_df)} records.")


