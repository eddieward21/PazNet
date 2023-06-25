# Import the required libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math
import numpy as np

# Read the CSV file 'emotion.csv' and select specific columns
df = pd.read_csv('../data/emotion.csv', usecols=['most frequent', 'second most', 'longest consecutive', 'label'])

# Vectorize the categorical columns by replacing their values with numeric equivalents
df['most frequent'].replace('fear', 0, inplace=True, regex=True)
df['most frequent'].replace('angry', 1, inplace=True, regex=True)
df['most frequent'].replace('disgust', 2, inplace=True, regex=True)
df['most frequent'].replace('sad', 3, inplace=True, regex=True)
df['most frequent'].replace('neutral', 4, inplace=True, regex=True)
df['most frequent'].replace('happy', 5, inplace=True, regex=True)
df['most frequent'].replace('surprise', 6, inplace=True, regex=True)

df['second most'].replace('fear', 0, inplace=True, regex=True)
df['second most'].replace('angry', 1, inplace=True, regex=True)
df['second most'].replace('disgust', 2, inplace=True, regex=True)
df['second most'].replace('sad', 3, inplace=True, regex=True)
df['second most'].replace('neutral', 4, inplace=True, regex=True)
df['second most'].replace('happy', 5, inplace=True, regex=True)
df['second most'].replace('surprise', 6, inplace=True, regex=True)

df['longest consecutive'].replace('fear', 0, inplace=True, regex=True)
df['longest consecutive'].replace('angry', 1, inplace=True, regex=True)
df['longest consecutive'].replace('disgust', 2, inplace=True, regex=True)
df['longest consecutive'].replace('sad', 3, inplace=True, regex=True)
df['longest consecutive'].replace('neutral', 4, inplace=True, regex=True)
df['longest consecutive'].replace('happy', 5, inplace=True, regex=True)
df['longest consecutive'].replace('surprise', 6, inplace=True, regex=True)

# Generate histograms of the vectorized columns
df.hist(bins=7, color='steelblue', edgecolor='black', linewidth=1.0, xlabelsize=8, ylabelsize=8, grid=False)
plt.show()

# Plot a countplot of the 'most frequent' column grouped by the 'label' column
cp = sns.countplot(x="most frequent", hue="label", data=df)
names = ['fear', 'angry', 'disgust', 'sad', 'neutral', 'happy', 'surprise']
plt.xticks([0,1,2,3,4,5,6], names, rotation=45)
plt.show()

# Plot a countplot of the 'second most' column grouped by the 'label' column
cp2 = sns.countplot(x="second most", hue="label", data=df)
names = ['fear', 'angry', 'sad', 'neutral', 'happy', 'surprise']
plt.xticks([0,1,2,3,4,5], names, rotation=45)
plt.show()

# Plot a countplot of the 'longest consecutive' column grouped by the 'label' column
cp3 = sns.countplot(x="longest consecutive", hue="label", data=df)
names = ['fear', 'angry', 'disgust', 'sad', 'neutral', 'happy', 'surprise']
plt.xticks([0,1,2,3,4,5,6], names, rotation=45)
plt.show()

# Create a feature dictionary mapping column indices to labels
feature_dict = {i: label for i, label in zip(
    range(3), (
        'most frequent', 'second most', 'longest consecutive'
    )
)}

X = df.iloc[:, :3].values  # Extract feature values
y = df['label'].values  # Extract target values

# Plot the distribution of feature values for each class separately
for i in range(3):
    plt.subplot(1, 3, i+1)
    sns.distplot(X[y=='no', i], hist=False, kde=True, color='darkblue', label='no')
    sns.distplot(X[y=='yes', i], hist=False, kde=True, color='red', label='yes')
    plt.xlabel(feature_dict[i], fontsize=12)
    plt.xticks([0,1,2,3,4,5,6], names, rotation=90)
plt.legend()
plt.show()

# Plot the distribution of feature values for the negative class (no)
for i in range(3):
    plt.subplot(1, 3, i+1)
    sns.distplot(X[y=='no', i], norm_hist=True, kde=False, color='darkblue', label='no', bins=7)
    plt.xlabel(feature_dict[i], fontsize=12)
    plt.xticks([0, 1, 2, 3, 4, 5, 6], names, rotation=90)
plt.legend()
plt.show()

# Plot the distribution of feature values for the positive class (yes)
for i in range(3):
    plt.subplot(1, 3, i+1)
    sns.distplot(X[y=='yes', i], norm_hist=True, kde=False, color='red', label='yes', bins=7)
    plt.xlabel(feature_dict[i], fontsize=12)
    plt.xticks([0,1,2,3,4,5,6], names, rotation=90)
plt.legend()
plt.show()

"""
This code performs data visualization and analysis on the df 
DataFrame using the matplotlib and seaborn libraries:
"""