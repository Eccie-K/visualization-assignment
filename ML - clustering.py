import pandas
df = pandas.read_csv('african_crises.csv')
print(df)

empties = df.isnull().sum()
print(empties)

subset = df[['exch_usd', 'inflation_annual_cpi']]

array = subset.values
X = array[:, 0:2]

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3, random_state = 42) #we do four clusters
model.fit_predict(X)
print('Learning//Done')