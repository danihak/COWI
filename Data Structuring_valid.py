# Importing required libraries
from zipfile import ZipFile
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------- Step 1: Extracting Files from ZIP Archive -------

zip_file_path = '/mnt/data/Karnataka.zip'
extraction_path = '/mnt/data/Karnataka'

with ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

extracted_files = os.listdir(extraction_path)

# ------- Step 2: Inspecting Columns in Each File -------

def get_columns(file_path):
    df = pd.read_excel(file_path, header=16)
    return df.columns.tolist()

files_columns = {file: get_columns(os.path.join(extraction_path, file)) for file in extracted_files}

# ------- Step 3: Creating Visualization Matrix of Columns -------

all_columns = [col for cols in files_columns.values() for col in cols]
unique_columns = list(set(all_columns))

viz_matrix = pd.DataFrame(columns=unique_columns, index=files_columns.keys())
viz_matrix.loc[:, :] = [[1 if col in columns else 0 for col in unique_columns] for columns in files_columns.values()]

# Visualizing the matrix
plt.figure(figsize=(15, 10))
sns.heatmap(viz_matrix.astype(int), cmap="Blues", annot=False, linewidths=.5)
plt.xlabel("Columns")
plt.ylabel("Files")
plt.title("Visualization Matrix of Columns Presence Across Files")
plt.xticks(rotation=90)
plt.show()

# ------- Step 4: Extracting Specific Data from Each File -------

def extract_specific_data(file_path):
    all_data = pd.read_excel(file_path, header=16, nrows=1659-16)
    data = pd.DataFrame()
    required_columns = ["From Date", "PM2.5", "PM10", "NO2", "SO2", "CO", "Ozone", "WS", "WD", "RH"]
    for col in required_columns:
        if col in all_data.columns:
            data[col] = all_data[col]
        else:
            data[col] = None
    
    city_station = pd.read_excel(file_path, header=None, usecols=[1], nrows=7)
    data["City Name"] = city_station.iloc[5, 0]
    data["Station Name"] = city_station.iloc[6, 0]
    
    return data

all_data = pd.concat([extract_specific_data(os.path.join(extraction_path, file)) for file in extracted_files], ignore_index=True)

# ------- Step 5: Saving the Extracted Data to a New CSV File -------

csv_file_path = '/mnt/data/compiled_extracted_data.csv'
all_data.to_csv(csv_file_path, index=False)

# Displaying the path to the new CSV file
csv_file_path
