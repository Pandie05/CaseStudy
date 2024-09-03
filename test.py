import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
file1 = 'csv\jail.csv'
file2 = 'csv\hs.csv'

#file1 = 'CaseStudy\csv\jail.csv'
#file2 = 'CaseStudy\csv\hs.csv'

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)


# Display the first few rows of each DataFrame to understand the structure
print("Data from first file:")
print(df1.head())
print("\nData from second file:")
print(df2.head())

# Plotting the data from the first file as a bar graph
df1.hist(figsize=(10, 6),bins=50)
plt.title('Data from First File')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend(loc='best')


# Plotting the data from the second file as a bar graph
df2.hist( figsize=(10, 6),bins=50)
plt.title('Data from Second File')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend(loc='best')
plt.show()
