# Import the required libraries
import pandas as pd
import numpy as np

# Read the CSV file 'emotion.csv' and select specific columns
df = pd.read_csv('/Users/wuxiaodong/Downloads/emotion.csv', usecols=['path', 'most frequent', 'second most', 'longest consecutive'])

# Sort the DataFrame by the 'path' column in ascending order and reset the index
df.sort_values('path', inplace=True, ignore_index=True)

# Specify the path of the label CSV file
path = '/Volumes/Samsung_T5/inagt_response_labels.csv'

# Read the label CSV file and select specific columns
label = pd.read_csv(path, usecols=['clipname', 'goodtime'])

# Create an empty list to store the labels
label_list = []

# Iterate over the rows of the 'df' DataFrame
for i in range(len(df)):
    # Extract the 'path' value from the current row
    txt = df.iloc[i, 0]
    
    # Extract the 'clip' value by removing the last 13 characters from 'txt'
    clip = txt[:-13]
    
    # Set a flag to indicate if a matching label is found
    flag = 0
    
    # Iterate over the rows of the 'label' DataFrame
    for j in range(len(label)):
        # Check if the 'clipname' value in 'label' matches 'clip'
        if label.iloc[j, 0] == clip:
            # Print 1 to indicate a match is found
            print(1)
            
            # Append the corresponding 'goodtime' value to 'label_list'
            label_list.append(label.iloc[j, 1])
            
            # Set the flag to 1 to indicate a match is found
            flag = 1
            
            # Exit the inner loop
            break
    
    # If no match is found, append NaN (missing value) to 'label_list'
    if flag == 0:
        label_list.append(np.nan)

# Assign the 'label_list' as a new column 'label' in the 'df' DataFrame
df = df.assign(label=label_list)

# Drop any rows in the 'df' DataFrame that have missing values (NaN)
df = df.dropna(how='any')

# Save the updated 'df' DataFrame to a new CSV file 'emotion.csv'
df.to_csv('emotion.csv')

# Print a blank line
print()
"""

Overall, the code seems to match labels from one CSV file (inagt_response_labels.csv) 
to another CSV file (emotion.csv) based on the clip names. It adds a new column 'label' 
to df containing the corresponding 'goodtime' values from label. The final DataFrame df
 is then saved to a new CSV file named 'emotion.csv'.
"""