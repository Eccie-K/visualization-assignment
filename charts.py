import pandas
df = pandas.read_csv('online_retail.csv', parse_dates=['InvoiceDate'])
df = df.set_index('InvoiceDate')
print(df)
empties = df.isnull().sum()

print(empties)

df['Customer ID'].fillna(0, inplace=True)
df['Customer ID'].replace({0:'Unknown'}, inplace=True)
df['Description'].fillna(1, inplace=True)
df['Description'].replace({1:"None"}, inplace=True)

newdates = pandas.to_datetime(['12-02-2010', '10-15-2010', '03-08-2010', '11-01-2010', 'Nov 05 10 05:33:26'])

print(newdates)

#online transactions in 2011

import matplotlib.pyplot as plt
df.loc['2011', 'Quantity'].plot()
plt.title('Number of online  transactions in 2011')
plt.xlabel('Year 2011')
plt.ylabel('Number of transactions')
plt.show()


df.loc['2011 - 7', 'Quantity'].plot()
plt.title('Number of online transactions in July 2011')
plt.xlabel('July 2011')
plt.ylabel('Number of transactions')
plt.show()









