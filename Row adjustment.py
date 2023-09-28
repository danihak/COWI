# Import Necessary Libraries
import pandas as pd
import os

# Step 1: Load the CSV File and Inspect Its Structure
file_path = '/mnt/data/combined_data_with_headers.csv'
inspection_df = pd.read_csv(file_path)

# Step 2: Identify Rows Where Headers Reappear
header_rows = inspection_df.index[inspection_df['From Date'] == 'From Date'].tolist()

# Step 3: Clean the DataFrame by Removing Repeated Headers
cleaned_df = inspection_df.drop(header_rows).reset_index(drop=True)

# Step 4: Save the Cleaned DataFrame to a New CSV File
cleaned_file_path = '/mnt/data/cleaned_combined_data.csv'
cleaned_df.to_csv(cleaned_file_path, index=False)

# Verify if the file is created and display the path
if os.path.exists(cleaned_file_path):
    print(f"The cleaned data has been saved to: {cleaned_file_path}")
else:
    print("There was an issue saving the cleaned data.")
