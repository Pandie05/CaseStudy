import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
jailcsv = 'csv/jail.csv'
hscsv = 'csv/hs.csv'
newjailcsv = 'csv/new_jail.csv'
newhscsv = 'csv/new_hs.csv'

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(jailcsv)
df2 = pd.read_csv(hscsv)
ndf1 = pd.read_csv(newjailcsv)
ndf2 = pd.read_csv(newhscsv)


#sort the data by the column cty
df1 = df1.sort_values(by='cty')
df2 = df2.sort_values(by='cty')

#------------------------------------------------------------JAIL------------------------------------------------------------

# Create a dictionary to store the state abbreviations and their corresponding mean values
jail_means = {
    'AL': df1['jailrate'].iloc[1:67].mean(),
    'AK': df1['jailrate'].iloc[68:96].mean(),
    'AZ': df1['jailrate'].iloc[97:111].mean(),
    'AR': df1['jailrate'].iloc[112:186].mean(),
    'CA': df1['jailrate'].iloc[187:244].mean(),
    'CO': df1['jailrate'].iloc[245:308].mean(),
    'CT': df1['jailrate'].iloc[309:316].mean(),
    'DE': df1['jailrate'].iloc[317:319].mean(),
    'FL': df1['jailrate'].iloc[320:386].mean(),
    'GA': df1['jailrate'].iloc[387:545].mean(),
    'HI': df1['jailrate'].iloc[546:550].mean(),
    'ID': df1['jailrate'].iloc[551:594].mean(),
    'IL': df1['jailrate'].iloc[595:695].mean(),
    'IN': df1['jailrate'].iloc[696:788].mean(),
    'IA': df1['jailrate'].iloc[789:887].mean(),
    'KS': df1['jailrate'].iloc[888:992].mean(),
    'KY': df1['jailrate'].iloc[993:1112].mean(),
    'LA': df1['jailrate'].iloc[1113:1176].mean(),
    'ME': df1['jailrate'].iloc[1177:1192].mean(),
    'MD': df1['jailrate'].iloc[1193:1216].mean(),
    'MA': df1['jailrate'].iloc[1217:1230].mean(),
    'MI': df1['jailrate'].iloc[1231:1312].mean(),
    'MN': df1['jailrate'].iloc[1313:1400].mean(),
    'MS': df1['jailrate'].iloc[1401:1482].mean(),
    'MO': df1['jailrate'].iloc[1483:1597].mean(),
    'MT': df1['jailrate'].iloc[1596:1653].mean(),
    'NE': df1['jailrate'].iloc[1654:1746].mean(),
    'NV': df1['jailrate'].iloc[1747:1763].mean(),
    'NH': df1['jailrate'].iloc[1764:1773].mean(),
    'NJ': df1['jailrate'].iloc[1774:1794].mean(),
    'NM': df1['jailrate'].iloc[1795:1827].mean(),
    'NY': df1['jailrate'].iloc[1828:1889].mean(),
    'NC': df1['jailrate'].iloc[1890:1989].mean(),
    'ND': df1['jailrate'].iloc[1990:2042].mean(),
    'OH': df1['jailrate'].iloc[2043:2130].mean(),
    'OK': df1['jailrate'].iloc[2131:2207].mean(),
    'OR': df1['jailrate'].iloc[2208:2243].mean(),
    'PA': df1['jailrate'].iloc[2245:2310].mean(),
    'RI': df1['jailrate'].iloc[2311:2315].mean(),
    'SC': df1['jailrate'].iloc[2316:2361].mean(),
    'SD': df1['jailrate'].iloc[2362:2427].mean(),
    'TN': df1['jailrate'].iloc[2428:2522].mean(),
    'TX': df1['jailrate'].iloc[2523:2776].mean(),
    'UT': df1['jailrate'].iloc[2777:2805].mean(),
    'VT': df1['jailrate'].iloc[2806:2818].mean(),
    'VA': df1['jailrate'].iloc[2819:2952].mean(),
    'WA': df1['jailrate'].iloc[2953:2993].mean(),
    'WV': df1['jailrate'].iloc[2992:3046].mean(),
    'WI': df1['jailrate'].iloc[3047:3118].mean(),
    'WY': df1['jailrate'].iloc[3119:3141].mean()
}

#turn to decimal
for key in jail_means:
    jail_means[key] = jail_means[key] * 100

#round
for key in jail_means:
    jail_means[key] = round(jail_means[key], 3)

#for key in jail_means:
    #print(key, ":", jail_means[key])

# Create a new DataFrame from the dictionary
ndf1 = pd.DataFrame(list(jail_means.items()), columns=['State', 'Mean'])

#------------------------------------------------------------HS------------------------------------------------------------

hs_means = {
    'AL': df2['hsrate'].iloc[1:67].mean(),
    'AK': df2['hsrate'].iloc[68:96].mean(),
    'AZ': df2['hsrate'].iloc[97:111].mean(),
    'AR': df2['hsrate'].iloc[112:186].mean(),
    'CA': df2['hsrate'].iloc[187:244].mean(),
    'CO': df2['hsrate'].iloc[245:308].mean(),
    'CT': df2['hsrate'].iloc[309:316].mean(),
    'DE': df2['hsrate'].iloc[317:319].mean(),
    'FL': df2['hsrate'].iloc[320:386].mean(),
    'GA': df2['hsrate'].iloc[387:545].mean(),
    'HI': df2['hsrate'].iloc[546:550].mean(),
    'ID': df2['hsrate'].iloc[551:594].mean(),
    'IL': df2['hsrate'].iloc[595:695].mean(),
    'IN': df2['hsrate'].iloc[696:788].mean(),
    'IA': df2['hsrate'].iloc[789:887].mean(),
    'KS': df2['hsrate'].iloc[888:992].mean(),
    'KY': df2['hsrate'].iloc[993:1112].mean(),
    'LA': df2['hsrate'].iloc[1113:1176].mean(),
    'ME': df2['hsrate'].iloc[1177:1192].mean(),
    'MD': df2['hsrate'].iloc[1193:1216].mean(),
    'MA': df2['hsrate'].iloc[1217:1230].mean(),
    'MI': df2['hsrate'].iloc[1231:1312].mean(),
    'MN': df2['hsrate'].iloc[1313:1400].mean(),
    'MS': df2['hsrate'].iloc[1401:1482].mean(),
    'MO': df2['hsrate'].iloc[1483:1597].mean(),
    'MT': df2['hsrate'].iloc[1596:1653].mean(),
    'NE': df2['hsrate'].iloc[1654:1746].mean(),
    'NV': df2['hsrate'].iloc[1747:1763].mean(),
    'NH': df2['hsrate'].iloc[1764:1773].mean(),
    'NJ': df2['hsrate'].iloc[1774:1794].mean(),
    'NM': df2['hsrate'].iloc[1795:1827].mean(),
    'NY': df2['hsrate'].iloc[1828:1889].mean(),
    'NC': df2['hsrate'].iloc[1890:1989].mean(),
    'ND': df2['hsrate'].iloc[1990:2042].mean(),
    'OH': df2['hsrate'].iloc[2043:2130].mean(),
    'OK': df2['hsrate'].iloc[2131:2207].mean(),
    'OR': df2['hsrate'].iloc[2208:2243].mean(),
    'PA': df2['hsrate'].iloc[2245:2310].mean(),
    'RI': df2['hsrate'].iloc[2311:2315].mean(),
    'SC': df2['hsrate'].iloc[2316:2361].mean(),
    'SD': df2['hsrate'].iloc[2362:2427].mean(),
    'TN': df2['hsrate'].iloc[2428:2522].mean(),
    'TX': df2['hsrate'].iloc[2523:2776].mean(),
    'UT': df2['hsrate'].iloc[2777:2805].mean(),
    'VT': df2['hsrate'].iloc[2806:2818].mean(),
    'VA': df2['hsrate'].iloc[2819:2952].mean(),
    'WA': df2['hsrate'].iloc[2953:2993].mean(),
    'WV': df2['hsrate'].iloc[2992:3046].mean(),
    'WI': df2['hsrate'].iloc[3047:3118].mean(),
    'WY': df2['hsrate'].iloc[3119:3141].mean()
}

#turn to decimal
for key in hs_means:
    hs_means[key] = hs_means[key] * 100

#round
for key in hs_means:
    hs_means[key] = round(hs_means[key], 3)

#for key in hs_means:
    #print(key, ":", hs_means[key])

# Create a new DataFrame from the dictionary
ndf2 = pd.DataFrame(list(hs_means.items()), columns=['State', 'Mean'])

#------------------------------------------------------------PLOTTING------------------------------------------------------------

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Plot the data from ndf1 on the first subplot
ax1.bar(ndf1['State'], ndf1['Mean'])
ax1.set_title('Jail Means')

# Plot the data from ndf2 on the second subplot
ax2.bar(ndf2['State'], ndf2['Mean'])
ax2.set_title('HS Means')

# Adjust the size of the subplots to make them appear the same size
plt.subplots_adjust(hspace=0.5)

# Display the plot
plt.show()