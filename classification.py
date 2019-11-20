import pandas

df = pandas.read_csv("bank_updated1.csv")
print(df)

import sklearn

subset = df[['exch_usd', 'inflation_annual_cpi', 'inflation_crises']]






array = subset.values
X = array[:, 0:3]  # -1 all rows all columns from 0 to the 8th. y is the 8th full colon means all rows e.g 0:30 means 0 - 30th row
y = array[:, 3]  # labeled - all rows


from imblearn.over_sampling import SMOTE
sm = SMOTE(ratio = 'auto', kind = 'regular', random_state = 42)

X_sampled, y_sampled = sm.fit_sample(X, y)
# we do not expose x and y to the model but we split, training data  and testing data...70% for traingng and 30% for testing

from sklearn import model_selection

X_train, X_test, y_train, y_test = model_selection.train_test_split(X_sampled, y_sampled,
                                                                    test_size=0.30,
                                                                    random_state=42)


#import models

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC

#TRAIN DATA
object = DecisionTreeClassifier()
print('Model training on this data')

object.fit(X_train, y_train)  # learning process
print("Done with training with 70% of data")

# once the model learns, ask the model to predict X_test

predictions = object.predict(X_test)
print(predictions)

model = LinearDiscriminantAnalysis()
model.fit(X_train, y_train)
print('Done learning from 70% of data')

#test your model
predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score, classification_report

print(accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, predictions))

print(subset.groupby('inflation_crises').size())

newperson = [[80, 5.4], [100, 7.2]] # is the person likely to
observation = model.predict(newperson)
print('Predicted', observation)