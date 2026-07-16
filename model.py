import pickle
import pandas as pd

df=pd.read_csv('iris.csv')
df
x= df.iloc[:,1:5]
y=df.iloc[:,5]
from sklearn.model_selection import train_test_split

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=15)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(x_train, y_train)

# create pickle dump
pickle.dump(knn,open("model.pkl","wb"))