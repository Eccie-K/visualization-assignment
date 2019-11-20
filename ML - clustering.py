#modcom.co.ke/advertising
import pandas
df = pandas.read_csv("african_crises.csv")
print(df)
print(df.shape)

empties = df.isnull().sum()
print(empties)

#filling empties and encoding where necessary
# no feature selection in clustering
subset = df[['exch_usd', 'inflation_annual_cpi']]

array = subset.values
X = array[:, 0:2] # no response y hence unsupervised

from sklearn.cluster import KMeans
model = KMeans(n_clusters=2, random_state =42) #we do four clusters
model.fit_predict(X)
print('Learning//Done')

#Get the means for each cluster and per column

centronoids = model.cluster_centers_

dataframe = pandas.DataFrame(centronoids, columns =['exch_usd', 'inflation_annual_cpi'])
print(dataframe)

# who is this cluster
#adding a column at the end
subset['label'] = model.labels_
subset = subset[subset['label'] == 2]
print(subset)

#generating excel worksheet

import xlwt
subset.to_excel('cluster3.xls', columns = ['exch_usd', 'inflation_annual_cpi'])

