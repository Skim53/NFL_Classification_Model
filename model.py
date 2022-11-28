#Initialization
import pandas as pd
import numpy as np 
import joblib
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#import dataset
df = pd.read_csv(r"C:\Users\17036\Documents\School\Fall_2022\CDS_303\Code\Streamlit\Master_DF_Changed_2020.csv")

# naming features used in the model
feature_cols = ['Offense Pass DVOA', 'Offense Rush DVOA', 'Offense Variance', 'Offense Schedule', 'Defense Pass DVOA', 'Defense Rush DVOA', 'Defense Variance', 'Defense Schedule']
# Features Converted into Numpy Array
X = df[feature_cols].to_numpy()
# Target variable Converted into Numpy Array
y = df.Playoffs.to_numpy()

#Training Set: 70%
#Training Set: 30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 16)

#Logistic Regression Model
lr = LogisticRegression(multi_class='multinomial', solver='lbfgs', random_state = 16)
# fit the model with data
lr.fit(X_train, y_train)

#prediction on the test set using predict()
y_pred = lr.predict(X_test)

#Accuracy of Logistic Regression classifer for Train and Test Sets
print('Accuracy of logistic regression classifier on train set: {:.2f}'.format(lr.score(X_train, y_train)))
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(lr.score(X_test, y_test)))

joblib.dump(lr, "lr_model.sav")
