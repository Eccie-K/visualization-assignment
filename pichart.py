#online retail transactions in 2011
import pandas
df = pandas.read_csv('online_retail.csv', parse_dates=['InvoiceDate'])
df = df.set_index('InvoiceDate')
print(df)
empties = df.isnull().sum()

print(empties)



import matplotlib.pyplot as plt


x = df.groupby('Country').size()

print(x)

x = df.groupby('Country').size().plot(kind = 'pie', autopct = '%1.1f%%')


plt.title('Transaction by Country')
plt.xlabel('')
plt.ylabel('')
plt.show()







