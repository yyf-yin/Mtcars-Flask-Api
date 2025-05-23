import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv('app/mtcars.csv')

# If the first column is non-numeric (like car name), drop it
if df.columns[0].lower() in ['model', 'car', 'name']:
    df = df.drop(columns=df.columns[0])

# Separate predictors and target
X = df.drop(columns=['mpg'])
y = df['mpg']

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
with open('app/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved to app/model.pkl")
