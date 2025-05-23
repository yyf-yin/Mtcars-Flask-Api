import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


df = pd.read_csv('app/mtcars.csv')
if df.columns[0].lower() in ['model', 'car', 'name']:
    df = df.drop(columns=df.columns[0])

X = df.drop(columns=['mpg'])
y = df['mpg']

model = LinearRegression()
model.fit(X, y)

with open('app/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved to app/model.pkl")
