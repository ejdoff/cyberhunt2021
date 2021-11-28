# Importing required libraries.
import pandas as pd
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
# %matplotlib inline
sns.set(color_codes=True)

datafile1 = 'data/freq_output/enp0s3-pvt-monday.pcap_Flow.csv'
datafile2 = 'data/freq_output/enp0s3-pvt-tuesday.pcap_Flow.csv'

df1 = pd.read_csv(datafile1)
df2 = pd.read_csv(datafile1)

# combining dataframes
concatenated = pd.concat([df1.assign(dataset='monday'), df2.assign(dataset='tuesday')])

# Dropping irrelevant payload columns
k = range(0,256)
for i in k:
    text1 = 'Payload' + str(i)
    del df1[text1]
    del df2[text1]
    del concatenated[text1]
    text2 = 'PayloadPerc' + str(i)
    del df1[text2]
    del df2[text2]
    del concatenated[text2]

# finding 0 values  --> weet niet wat dit nu eigenlijk zegt
# print(df1.isnull().sum())
# print(df2.isnull().sum())
print(concatenated.isnull().sum())

# boxplots !
for column in df1:
    if df1.dtypes[column] != 'object':
        # sns.boxplot(y=df1[column])
        # sns.boxplot(y=df2[column])
        # sns.boxplot(y=concatenated[column], data=concatenated) # nog niet lekker werkend
        plt.show()


# Finding the relations between the variables:  Heatmap
c1 = df1.corr()
c2 = df2.corr()
# plt.figure(figsize=(20,10))
# sns.heatmap(c1,annot=False)
# plt.show()
# plt.figure(figsize=(20,10))
# sns.heatmap(c2,annot=False)
# plt.show()


# finding correlation between two variables: scatterplots
# sns.scatterplot(x=df1['ACK Flag Count'], y=df2['ACK Flag Count'])
# plt.show()


for column1 in df1:  # cpu overload
    for column2 in df1:
        if df1.dtypes[column1] and df1.dtypes[column2] != 'object':
            fig, ax = plt.subplots(figsize=(10,6))
            # ax.scatter(df1[column1], df1[column2])
            sns.scatterplot(x=df1[column1], y=df1[column2])
            plt.show()