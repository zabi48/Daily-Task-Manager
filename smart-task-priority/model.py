import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("data.csv")

X = data[["deadline", "importance", "effort"]]

y = data["priority"]

model = DecisionTreeClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")