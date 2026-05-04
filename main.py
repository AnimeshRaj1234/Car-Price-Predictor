import pandas as pd
import pickle

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv("./data/cardata.csv")

# -------------------------------
# Preprocessing
# -------------------------------
df.drop(['Car_Name'], axis=1, inplace=True)

# Feature Engineering
df['Car_Age'] = 2026 - df['Year']
df.drop(['Year'], axis=1, inplace=True)

# Convert categorical to numerical
df = pd.get_dummies(df, drop_first=True)

# -------------------------------
# Split data
# -------------------------------
X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Train model
# -------------------------------
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X_train, y_train)

# -------------------------------
# Save model + columns
# -------------------------------
pickle.dump(model, open('model/car_price_model.pkl', 'wb'))
pickle.dump(X.columns, open('model/model_columns.pkl', 'wb'))

print("✅ Model trained and saved successfully!")