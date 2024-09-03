import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
file1 = 'CaseStudy\csv\jail.csv'
file2 = 'CaseStudy\csv\hs.csv'

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

#sort the data by the column cty
df1 = df1.sort_values(by='cty')
df2 = df2.sort_values(by='cty')

# sort the actual csv file by the column cty
df1.to_csv('CaseStudy\csv\jail.csv', index=False)
df2.to_csv('CaseStudy\csv\hs.csv', index=False)
