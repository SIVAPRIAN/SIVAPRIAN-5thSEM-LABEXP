# Botnet Attack Detection using Public Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Load dataset (example: botnet traffic dataset CSV)
# Replace with actual dataset file (e.g., "CTU13.csv", "CICIDS2017.csv")
data = pd.read_csv("botnet_dataset.csv")
print("Dataset Shape:", data.shape)
print("Columns:", data.columns)

# Step 2: Preprocessing
# Assuming dataset has features and a "Label" column (Normal or Botnet)
X = data.drop("Label", axis=1)
y = data["Label"]

# Convert categorical labels to binary (0 = Normal, 1 = Botnet)
y = y.replace({"Normal": 0, "Botnet": 1})

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train Random Forest Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 5: Predictions
y_pred = clf.predict(X_test)

# Step 6: Evaluation
print("\n=== Botnet Detection Results ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
