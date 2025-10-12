import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import os

df = pd.read_csv("data/processed/books_clean.csv")
print(f"Loaded {len(df)} books for classification")

X_train, X_test, y_train, y_test = train_test_split(
df["title"], 
 df["label"], 
test_size=0.2,
random_state=42,
  stratify=df["label"]
)

vec = TfidfVectorizer()
X_train_vec = vec.fit_transform(X_train)
X_test_vec = vec.transform(X_test)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_vec, y_train)

y_pred = clf.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.3f}")
print(classification_report(y_test, y_pred))

os.makedirs("logs", exist_ok=True)
pd.DataFrame([{"accuracy": acc}]).to_csv("logs/metrics.csv", index=False)
print("Metrics saved to logs/metrics.csv")
