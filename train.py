import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import RobustScaler

from sklearn.linear_model import LogisticRegression

import pickle

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("./heart.csv")

d = {}
cat_cols = []
num_cols = []
target_col = []
for i in list(df.columns):
    d[i] = df[i].value_counts().shape[0]
    
    if i == "output":
      target_col.append(i)

    elif df[i].value_counts().shape[0] < 10:
      cat_cols.append(i)
    else:
      num_cols.append(i)

df1 = df
# encoding the categorical columns
df1 = pd.get_dummies(df1, columns = cat_cols, drop_first = True)

# defining the features and target
X = df1.drop(['output'],axis=1)
y = df1[['output']]

# instantiating the scaler
scaler = RobustScaler()

# scaling the numerical features
X[num_cols] = scaler.fit_transform(X[num_cols])

X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)
X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, test_size=0.25, random_state=11)
print(len(df), len(X_full_train), len(X_train), len(X_val), len(X_test))

lr = LogisticRegression(C=0.0006951927961775605,
    penalty='none',
    solver='lbfgs',
    tol=0.23357214690901212,
    random_state=42)
lr.fit(X_train, y_train)

y_pred = lr.predict_proba(X_val)[:, 1]
roc_auc_score(y_val, y_pred)

y_pred = lr.predict_proba(X_full_train)[:, 1]
roc_auc_score(y_full_train, y_pred)

output_file = 'final_model_lr.bin'

f_out = open(output_file, 'wb') 
pickle.dump(lr, f_out)
f_out.close()

with open(output_file, 'wb') as f_out: 
    pickle.dump(lr, f_out)