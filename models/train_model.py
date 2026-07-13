import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "bridge_digital_twin_dataset.csv"

df = pd.read_csv(DATA_PATH)

# ---------------------------------------------------
# Features
# ---------------------------------------------------

X = df.drop(columns=["failure_probability"])

# Target

y = df["failure_probability"]

# Save feature order for prediction

joblib.dump(
    list(X.columns),
    "feature_columns.pkl"
)

# ---------------------------------------------------
# Train Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------
# Random Forest
# ---------------------------------------------------

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=18,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

predictions = model.predict(X_test)

# ---------------------------------------------------
# Evaluation
# ---------------------------------------------------

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = mse ** 0.5

r2 = r2_score(y_test, predictions)

print()

print("="*50)

print("Random Forest Performance")

print("="*50)

print(f"MAE : {mae:.5f}")

print(f"MSE : {mse:.5f}")

print(f"RMSE: {rmse:.5f}")

print(f"R²  : {r2:.5f}")

print()

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

joblib.dump(
    {
        "model": model,
        "feature_names": list(X.columns),
    },
    "models/random_forest.pkl",
)
print("Model saved successfully.")