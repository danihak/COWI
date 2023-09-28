# Import Necessary Libraries
import pandas as pd
import zipfile
import os

# Specify the State and Zip File Path
state_name = "YourStateName"  # Change this to the desired state name
zip_file_path = f"/mnt/data/{state_name}.zip"  # Update the file path accordingly

# Directory to Extract the Zip File
extraction_directory = f"/mnt/data/{state_name}"

# Unzip the File
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(extraction_directory)

# List All Extracted Files
extracted_files = os.listdir(extraction_directory)

# Adjusted Start and End Rows to Include Headers
adjusted_start_row = 15  # Excel row 16
correct_end_row = 1659   # Excel row 1660

# Specified Columns to Include in the CSV
specified_columns = [
    "From Date", "To Date", "PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "SO2", 
    "CO", "Ozone", "Benzene", "Toluene", "Eth-Benzene", "MP-Xylene", "O-Xylene", 
    "RH", "WS", "WD", "Xylene", "AT"
]

# Function to Extract Data Including Specified Columns and Write to New CSV File
def extract_and_write_data_with_headers_to_csv(file_path, start_row, end_row, new_csv_path, columns):
    df = pd.read_excel(file_path, skiprows=range(start_row), nrows=end_row - start_row + 1, header=0)
    file_name = os.path.basename(file_path)
    station_name, city_name = file_name.split('_')[0].split(', ')
    
    # Ensuring all specified columns are included
    for col in columns:
        if col not in df.columns:
            df[col] = None
    
    df['City'] = city_name
    df['Full Station Name'] = station_name
    mode = 'w' if not os.path.exists(new_csv_path) else 'a'
    header = True if mode == 'w' else False
    df.to_csv(new_csv_path, mode=mode, header=header, index=False, columns=columns + ['City', 'Full Station Name'])

# Create a New CSV File Path for Data Including Headers
new_csv_file_with_headers_path = f'/mnt/data/combined_data_with_headers_{state_name}.csv'

# Extract Data Including Headers and Write to New CSV File for Each File
for file in extracted_files:
    extract_and_write_data_with_headers_to_csv(
        os.path.join(extraction_directory, file), 
        adjusted_start_row, 
        correct_end_row, 
        new_csv_file_with_headers_path,
        specified_columns
    )

# Confirm That New CSV File with Headers Has Been Created and Data Has Been Appended
file_exists = os.path.exists(new_csv_file_with_headers_path)
file_size = os.path.getsize(new_csv_file_with_headers_path)

print(f"File Exists: {file_exists}, File Size: {file_size}")
