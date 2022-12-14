# -*- coding: utf-8 -*-
"""AIFinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_oMJgaUSqajBCdjkKXLHt4kNOgt-1mri
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn import metrics

from google.colab import files
tv_price_dataset = files.upload()

import io
tv_price_dataset2 = pd.read_csv(io.BytesIO(tv_price_dataset['Dataset.csv']))

tv_price_dataset3 = tv_price_dataset2.head(333)
tv_price_dataframe = tv_price_dataset3.iloc[:, :12]

tv_price_dataframe.replace({'Brand':{'LG':10,'Sony':11,'Walton':6,'Vision':7,'Samsung':12,'Xiaomi Mi':9, 'MyOne':1, 
                                     'Marcel':2, 'Konka':8, 'Jamuna':5, 'Minister':4, 'Singer':3}},inplace=True)
tv_price_dataframe.replace({'DeviceType':{'QLED':7,'OLED':6,'UHD':5,'LED':4,'LCD':3,'FHD':2, 'CRT':1}},inplace=True)
tv_price_dataframe.replace({'SpeakerSystem':{'4.2Channel':5,'4.0Channel':4,'2.2Channel':3,'2.0Channel':2,'Integrated':1}},inplace=True)
tv_price_dataframe.replace({'Resolution':{'4320x2160':6,'3840x2160':5,'1920x1080':4,'1366x768':3,'1280x720':2,'720x576':1,}},inplace=True)
tv_price_dataframe.replace({'Resolution\nupscaler':{'4KUHD':6,'4KHDR':5,'4K':4,'FHD':3,'HD':2,'SD':1}},inplace=True)

correlation = tv_price_dataframe.corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

# Splitting data
X = tv_price_dataframe.drop('Price', axis=1)
Y = tv_price_dataframe['Price']

# Splitting train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3, random_state = 2)
from sklearn import preprocessing
lbl = preprocessing.LabelEncoder()
X_train['Resolution'] = lbl.fit_transform(X_train['Resolution'].astype(str))
X_train['Resolution\nupscaler'] = lbl.fit_transform(X_train['Resolution\nupscaler'].astype(str))

# LINEAR REGRESSION
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_test)

plt.figure(figsize=(10,10))
plt.scatter(Y_test,Y_pred,s=15)
plt.xlabel('Actual',fontsize=14)
plt.ylabel('Predict',fontsize=14)
plt.title('Linear Regression Actual vs Predict')
plt.show()

df2 = pd.DataFrame({'Actual': Y_test, 'Predicted': Y_pred})
df2.plot(kind='bar',figsize=(10,8),xlabel='Test Data',ylabel='Ratings',title='Linear Regression')
plt.show()

print("Linear Regression Score: ",regressor.score(X_train, Y_train))
print('Mean Absolute Error:', 	metrics.mean_absolute_error(Y_test, Y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, Y_pred))
print('R2 Score:', metrics.r2_score(Y_test, Y_pred))

#X_test['Resolution'] = lbl.fit_transform(X_test['Resolution'].astype(str))
#X_test['Resolution\nupscaler'] = lbl.fit_transform(X_test['Resolution\nupscaler'].astype(str))

# XGBOOST
xgboost = XGBRegressor()
xgboost.fit(X_train, Y_train)
training_data_prediction = xgboost.predict(X_test)

plt.figure(figsize=(10,10))
plt.scatter(Y_test,training_data_prediction,s=15)
plt.xlabel('Actual',fontsize=14)
plt.ylabel('Predict',fontsize=14)
plt.title('XGBoost Actual vs Predict')
plt.show()

df3 = pd.DataFrame({'Actual': Y_test, 'Predicted': training_data_prediction})
df3.plot(kind='bar',figsize=(10,8),xlabel='Test Data',ylabel='Ratings',title='XGBoost')
plt.show()

print("XGBoost Regression Score: ",xgboost.score(X_train, Y_train))
print('Mean Absolute Error:', 	metrics.mean_absolute_error(Y_test, training_data_prediction))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, training_data_prediction))
print('R2 Score:', metrics.r2_score(Y_test, training_data_prediction))

"""Lasso Regression"""

# Lasso Regression
lassoreg = Lasso()
lassoreg.fit(X_train, Y_train)
training_lasso = lassoreg.predict(X_test)

plt.figure(figsize=(10,10))
plt.scatter(Y_test,training_lasso,s=15)
plt.xlabel('Actual',fontsize=14)
plt.ylabel('Predict',fontsize=14)
plt.title('Lasso Regression Actual vs Predict')
plt.show()

df3 = pd.DataFrame({'Actual': Y_test, 'Predicted': training_lasso})
df3.plot(kind='bar',figsize=(10,8),xlabel='Test Data',ylabel='Ratings',title='Lasso')
plt.show()

print("Lasso Regression Score: ",lassoreg.score(X_train, Y_train))
print('Mean Absolute Error:', 	metrics.mean_absolute_error(Y_test, training_lasso))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, training_lasso))
print('R2 Score:', metrics.r2_score(Y_test, training_lasso))

"""RANDOM FORREST"""

# Random Forrest
randomforrest = RandomForestRegressor(n_estimators=100)
randomforrest.fit(X_train, Y_train)
training_randomforrest = randomforrest.predict(X_test)

plt.figure(figsize=(10,10))
plt.scatter(Y_test,training_randomforrest,s=15)
plt.xlabel('Actual',fontsize=14)
plt.ylabel('Predict',fontsize=14)
plt.title('Random Forrest Actual vs Predict')
plt.show()

df3 = pd.DataFrame({'Actual': Y_test, 'Predicted': training_randomforrest})
df3.plot(kind='bar',figsize=(10,8),xlabel='Test Data',ylabel='Ratings',title='Random Forrest')
plt.show()

print("Random Forrest Score: ",randomforrest.score(X_train, Y_train))
print('Mean Absolute Error:', 	metrics.mean_absolute_error(Y_test, training_randomforrest))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, training_randomforrest))
print('R2 Score:', metrics.r2_score(Y_test, training_randomforrest))

"""Support Vector Machine"""

# Support Vector Machine
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X_train, Y_train)
training_knn= neigh.predict(X_test)

plt.figure(figsize=(10,10))
plt.scatter(Y_test,training_knn,s=15)
plt.xlabel('Actual',fontsize=14)
plt.ylabel('Predict',fontsize=14)
plt.title('KNN Actual vs Predict')
plt.show()

df3 = pd.DataFrame({'Actual': Y_test, 'Predicted': training_knn})
df3.plot(kind='bar',figsize=(10,8),xlabel='Test Data',ylabel='Ratings',title='KNN')
plt.show()

print("KNN Score: ",neigh.score(X_train, Y_train))
print('Mean Absolute Error:', 	metrics.mean_absolute_error(Y_test, training_knn))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, training_knn))
print('R2 Score:', metrics.r2_score(Y_test, training_knn))

