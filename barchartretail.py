# Bar chart to find out quantity of transactions by country
import pandas
df = pandas.read_csv('online_retail.csv', parse_dates=['InvoiceDate'])
df = df.set_index('InvoiceDate')
print(df)

empties = df.isnull().sum()
print(empties)

import matplotlib.pyplot as plt
z = df.groupby('Country')['Quantity'].mean()
print(z)

df.groupby('Country')['Quantity'].mean().plot(kind = 'bar', color = 'green')
plt.title('Number of Orders by Country')
plt.xlabel('Country')
plt.ylabel('Quantity')
plt.show()

# Scatter plot for quantity vs price

figure, ax = plt.subplots()
ax.scatter(df['Quantity'], df['Price'], color = 'blue', s=30)

ax.plot([df['Quantity'].min(), df['Quantity'].max()],
        [df['Price'].min(), df['Price'].max()], color = 'green')

ax.set_title("Relations of Quantity vs Price")
ax.set_xlabel("Quantity")
ax.set_ylabel("Price")
plt.show()


#heat maps

import seaborn

y = df[['StockCode', 'Quantity', 'Price', 'Customer ID', 'Country']]
figure, ax = plt.subplots()
seaborn.heatmap(df.corr(), cmap = 'Greens', annot = True)
plt.show()

#Normality - Normal distribution
#Checking distribution of numeric variables
# Check if normally distributed or not

figure, ax = plt.subplots()
ax.hist(df['Price'], color = 'green', label = 'Price', alpha = 0.75)
ax.hist(df['Quantity'], color = 'red', label = 'Quantity', alpha = 0.75)

ax.legend(loc = 'best')
ax.set_title('Distribution of Price')
ax.set_xlabel('unit')
ax.set_ylabel('Freq')
plt.show()


