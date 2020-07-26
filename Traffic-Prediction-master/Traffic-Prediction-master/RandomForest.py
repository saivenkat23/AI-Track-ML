import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the training dataset
path1 ="E:\\AI\\Book.csv"
train_dataset = pd.read_csv(path1)
X_train = train_dataset.iloc[:, [2,3,4,5]].values
y_train = train_dataset.iloc[:, 6].values
X_train
y_train

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X_train[:, 0] = labelencoder_X.fit_transform(X_train[:, 0])
X_train

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
X_train[:, 0] = labelencoder_X.fit_transform(X_train[:, 0])
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0])],remainder='passthrough')
X_train = np.array(ct.fit_transform(X_train))
X_train
X_train[:, 1] = labelencoder_X.fit_transform(X_train[:, 1])
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [2])],remainder='passthrough')
X_train = np.array(ct.fit_transform(X_train))
X_train
X_train[:, 4] = labelencoder_X.fit_transform(X_train[:, 4])
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [4])],remainder='passthrough')
X_train = np.array(ct.fit_transform(X_train))
X_train
X_train[:, 5] = labelencoder_X.fit_transform(X_train[:, 5])
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [5])],remainder='passthrough')
X_train = np.array(ct.fit_transform(X_train))
X_train

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)



from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_train)

output=clf.predict([X_train[34]])
print("The Effect of Traffic : ",output)
# Making the Confusion Matrix
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_train, y_pred)
print("Accuracy (in percentage) : ",ac*100)

