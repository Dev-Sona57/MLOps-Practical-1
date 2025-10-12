import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import joblib
import os

# Load dataset
df = pd.read_csv("data/processed/books_clean.csv")
print(f"Loaded {len(df)} books for classification")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["title"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

# Vectorize text
vec = TfidfVectorizer()
X_train_vec = vec.fit_transform(X_train)
X_test_vec = vec.transform(X_test)

# Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test_vec)
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")
print(metrics.classification_report(y_test, y_pred))

# Save metrics
os.makedirs("logs", exist_ok=True)
pd.DataFrame({
    "accuracy": [accuracy]
}).to_csv("logs/metrics.csv", index=False)
print("Metrics saved to logs/metrics.csv")

# Save model and vectorizer
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/model.pkl")
joblib.dump(vec, "models/vectorizer.pkl")

print("Model and vectorizer saved in 'models/'")

