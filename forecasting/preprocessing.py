# Import the required libraries
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import os

# Define a function to load data from a given path (default path is '/Volumes/Samsung_T5/INAGT_clean/m028/m028_final.csv')
def load_data(path='/Volumes/Samsung_T5/INAGT_clean/m028/m028_final.csv'):
    # Read the data from the specified path into a DataFrame
    data = pd.read_csv(path)

    # Create a DataFrame 'df' with specific columns from the data
    df = pd.DataFrame(data, columns=["timestamp", "accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ",
                                     "emp_accelX", "emp_accelY", "emp_accelZ", "BVP",
                                     "HR", "EDA", "TEMP", "IBI", "Vehicle speed", "Accelerator pedal angle",
                                     "Parked condition",
                                     "Brake oil pressure", "Steering signal"])

    # Interpolate missing values in the DataFrame
    df = df.interpolate()

    # Fill remaining missing values using forward filling (ffill) and backward filling (bfill)
    df = df.fillna(method="ffill")
    df = df.fillna(method="bfill")

    # Remove the 'timestamp' column from the DataFrame
    df.drop('timestamp', axis=1, inplace=True)

    # Resampling code
    ratio = int(504/10)  # Calculate the resampling ratio
    print(df.columns)
    for column in df.columns:
        # Resample each column in the DataFrame by applying signal.resample function
        df[column] = pd.Series(signal.resample(df[column], int(len(df[column])/ratio)))

    # Drop rows with all missing values
    df = df.dropna(how='all')

    print(len(df))

    return df

"""
The code defines a function load_data that reads and preprocesses data from a given file path. 
It loads the data into a DataFrame, performs interpolation and filling for missing values, 
removes unnecessary columns, and resamples the data. The function returns the processed DataFrame.
"""