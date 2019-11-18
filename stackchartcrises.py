import pandas
df = pandas.read_csv('african_crises.csv')
print(df)

empties = df.isnull().sum()
print(empties)

df['systemic_crisis'].replace({0:'no crisis', 1:'crisis'}, inplace = True)
df['domestic_debt_in_default'].replace({0:'no domestic debt', 1:'domestic debt'}, inplace = True)
df['sovereign_external_debt_default'].replace({0:'no sovereign debt', 1:'sovereign debt'}, inplace = True)
df['independence'].replace({0:'no independence', 1:'independence'}, inplace = True)
df['currency_crises'].replace({0:'no crisis', 1:'crisis'}, inplace = True)
df['inflation_crises'].replace({0:'no crisis', 1:'crisis'}, inplace = True)
df['banking_crisis'].replace({0:'no crisis', 1:'crisis'}, inplace = True)

import matplotlib.pyplot as plt
# pie chart to show banking crisis

x = df.groupby('banking_crisis').size().plot(kind = 'pie', autopct = '%1.1f%%',
                                            explode = ( 0,0.2))

plt.title('state of banking crisis')
plt.xlabel('')
plt.ylabel('')
plt.show()

y = df.groupby('independence').size().plot(kind = 'pie', autopct = '%1.1f%%',
                                            explode = ( 0,0.2))

plt.title('state of independence')
plt.xlabel('')
plt.ylabel('')
plt.show()


#z = df.groupby('country')['sovereign_external_debt_default'].mean()
#print(z)

#df.groupby('country')['sovereign_external_debt_default'].mean().plot(kind = 'bar', color = 'green')
#plt.title('Debt by country')
#plt.xlabel('Country')
#plt.ylabel('Debt')
#plt.show()



import seaborn

a = df[['sovereign_external_debt_default', 'gdp_weighted_default', 'inflation_annual_cpi']]
figure, ax = plt.subplots()
seaborn.heatmap(df.corr(), cmap = 'Greens', annot = True)
plt.show()


#Distribution of domestic debt vs sovereign debt

figure, ax = plt.subplots()
ax.hist(df['domestic_debt_in_default'], color = 'blue', label = 'domestic_debt_in_default', alpha = 0.75)
ax.hist(df['sovereign_external_debt_default'], color = 'red', label = 'sovereign_external_debt_default', alpha = 0.75)
ax.legend(loc = 'best')
ax.set_title('Distribution of domestic debt vs sovereign debt')
ax.set_xlabel('Debt')
ax.set_ylabel('Freq')
plt.show()

#scatter plot

figure, ax = plt.subplots()
ax.scatter(df['year'], df['exch_usd'], color = 'purple', s = 30)

ax.set_title('country vs exchange rate usd')
ax.set_xlabel('year')
ax.set_ylabel('exchange rate')
plt.show()
















