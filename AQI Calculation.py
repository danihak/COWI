#Loading and inspecting dataset 

import pandas as pd

# Load the dataset
aqi_data = pd.read_csv("/mnt/data/transformed_aqi_data(corrected).csv")

# Display the first few rows of the dataset
aqi_data.head()


#Sub-Indexing of PM2.5

def calculate_pm2_5_sub_index(pm2_5):
    """Calculate sub-index for PM2.5 based on provided formula."""
    if pd.isna(pm2_5) or isinstance(pm2_5, str):
        return 0
    elif pm2_5 <= 30:
        return pm2_5 * 50 / 30
    elif 30 < pm2_5 <= 60:
        return 50 + (pm2_5 - 30) * 50 / 30
    elif 60 < pm2_5 <= 90:
        return 100 + (pm2_5 - 60) * 100 / 30
    elif 90 < pm2_5 <= 120:
        return 200 + (pm2_5 - 90) * 100 / 30
    elif 120 < pm2_5 <= 250:
        return 300 + (pm2_5 - 120) * 100 / 130
    else:
        return 400 + (pm2_5 - 250) * 100 / 130

# Apply the function to the 'PM2.5' column to calculate its sub-index
aqi_data['PM2.5_Sub_Index'] = aqi_data['PM2.5'].apply(calculate_pm2_5_sub_index)

# Display the first few rows to verify
aqi_data[['PM2.5', 'PM2.5_Sub_Index']].head()





#Sub-Indexing of PM10

def calculate_pm10_sub_index(pm10):
    """Calculate sub-index for PM10 based on provided formula."""
    if pd.isna(pm10) or isinstance(pm10, str):
        return 0
    elif pm10 <= 50:
        return pm10
    elif 50 < pm10 <= 100:
        return pm10
    elif 100 < pm10 <= 250:
        return 100 + (pm10 - 100) * 100 / 150
    elif 250 < pm10 <= 350:
        return 200 + (pm10 - 250)
    elif 350 < pm10 <= 430:
        return 300 + (pm10 - 350) * 100 / 80
    else:
        return 400 + (pm10 - 430) * 100 / 80

# Apply the function to the 'PM10' column to calculate its sub-index
aqi_data['PM10_Sub_Index'] = aqi_data['PM10'].apply(calculate_pm10_sub_index)

# Display the first few rows to verify
aqi_data[['PM10', 'PM10_Sub_Index']].head()

#Sub-Indexing of NO2

def calculate_NO2_sub_index(NO2):
    """Calculate sub-index for NO2 based on provided formula."""
    if pd.isna(NO2) or isinstance(NO2, str):
        return 0
    elif NO2 <= 40:
        return NO2 * 50 / 40
    elif 40 < NO2 <= 80:
        return 50 + (NO2 - 40) * 50 / 40
    elif 80 < NO2 <= 180:
        return 100 + (NO2 - 80) * 100 / 100
    elif 180 < NO2 <= 280:
        return 200 + (NO2 - 180) * 100 / 100
    elif 280 < NO2 <= 400:
        return 300 + (NO2 - 280) * 100 / 120
    else:
        return 400 + (NO2 - 400) * 100 / 120
# Apply the function to the 'NO2' column to calculate its sub-index
aqi_data['NO2_Sub_Index'] = aqi_data['NO2'].apply(calculate_NO2_sub_index)

# Display the first few rows to verify   aqi_data[['NO2', 'NO2_Sub_Index']].head()

#Sub-Indexing of SO2

def calculate_so2_sub_index(so2):
    """Calculate sub-index for SO2 based on provided formula."""
    if pd.isna(so2) or isinstance(so2, str):
        return 0
    elif so2 <= 40:
        return so2 * 50 / 40
    elif 40 < so2 <= 80:
        return 50 + (so2 - 40) * 50 / 40
    elif 80 < so2 <= 380:
        return 100 + (so2 - 80) * 100 / 300
    elif 380 < so2 <= 800:
        return 200 + (so2 - 380) * 100 / 420
    elif 800 < so2 <= 1600:
        return 300 + (so2 - 800) * 100 / 800
    else:
        return 400 + (so2 - 1600) * 100 / 800
# Apply the function to the 'SO2' column to calculate its sub-index
aqi_data['SO2_Sub_Index'] = aqi_data['SO2'].apply(calculate_so2_sub_index)

# Display the first few rows to verify
aqi_data[['SO2', 'SO2_Sub_Index']].head()

#Sub-Indexing of CO

def calculate_co_sub_index(co):
    """Calculate sub-index for CO based on provided formula."""
    if pd.isna(co) or isinstance(co, str):
        return 0
    elif co <= 1:
        return co * 50 / 1
    elif 1 < co <= 2:
        return 50 + (co - 1) * 50 / 1
    elif 2 < co <= 10:
        return 100 + (co - 2) * 100 / 8
    elif 10 < co <= 17:
        return 200 + (co - 10) * 100 / 7
    elif 17 < co <= 34:
        return 300 + (co - 17) * 100 / 17
    else:
        return 400 + (co - 34) * 100 / 17
# Apply the function to the 'CO' column to calculate its sub-index
aqi_data['CO_Sub_Index'] = aqi_data['CO'].apply(calculate_co_sub_index)

# Display the first few rows to verify
aqi_data[['CO', 'CO_Sub_Index']].head()

#Sub-Indexing of Ozone

def calculate_ozone_sub_index(ozone):
    """Calculate sub-index for Ozone based on provided formula."""
    if pd.isna(ozone) or isinstance(ozone, str):
        return 0
    elif ozone <= 50:
        return ozone * 50 / 50
    elif 50 < ozone <= 100:
        return 50 + (ozone - 50) * 50 / 50
    elif 100 < ozone <= 168:
        return 100 + (ozone - 100) * 100 / 68
    elif 168 < ozone <= 208:
        return 200 + (ozone - 168) * 100 / 40
    elif 208 < ozone <= 748:
        return 300 + (ozone - 208) * 100 / 539
    else:
        return 400 + (ozone - 748) * 100 / 539
# Apply the function to the 'Ozone' column to calculate its sub-index
aqi_data['Ozone_Sub_Index'] = aqi_data['Ozone'].apply(calculate_ozone_sub_index)
# Display the first few rows to verify
aqi_data[['Ozone', 'Ozone_Sub_Index']].head()

#Data Quality Check 

def data_quality_check(value):
    """Apply data quality check based on provided formula."""
    if pd.isna(value) or isinstance(value, str) or value <= 0:
        return 0
    else:
        return 1

# List of pollutants to check
pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Ozone']

# Apply data quality check for each pollutant
for pollutant in pollutants:
    aqi_data[f'{pollutant}_Quality'] = aqi_data[pollutant].apply(data_quality_check)

# Display the first few rows to verify
aqi_data[['PM2.5', 'PM2.5_Quality', 'PM10', 'PM10_Quality', 'NO2', 'NO2_Quality', 'SO2', 'SO2_Quality', 'CO', 'CO_Quality', 'Ozone', 'Ozone_Quality']].head()



#Calculating AQI

def calculate_aqi(row):
    """Calculate AQI based on provided formula."""
    quality_checks = [row['PM2.5_Quality'], row['PM10_Quality'], row['NO2_Quality'], 
                      row['SO2_Quality'], row['CO_Quality'], row['Ozone_Quality']]
    
    # Check for at least 3 good inputs
    if (row['PM2.5_Quality'] == 1 or row['PM10_Quality'] == 1) and sum(quality_checks) >= 3:
        return max(row['PM2.5_Sub_Index'], row['PM10_Sub_Index'], row['NO2_Sub_Index'], 
                   row['SO2_Sub_Index'], row['CO_Sub_Index'], row['Ozone_Sub_Index'])
    else:
        return "Atleast 3 inputs*"

# Calculate AQI for each row
aqi_data['AQI'] = aqi_data.apply(calculate_aqi, axis=1)

# Display the first few rows to verify
aqi_data[['PM2.5_Sub_Index', 'PM10_Sub_Index', 'NO2_Sub_Index', 'SO2_Sub_Index', 'CO_Sub_Index', 'Ozone_Sub_Index', 'AQI']].head()


#Saving the workbook

# Save the enriched dataset to a new CSV file
file_path = "/mnt/data/enriched_aqi_data.csv"
aqi_data.to_csv(file_path, index=False)

file_path
