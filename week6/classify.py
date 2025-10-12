import joblib
import os

# Create folder 'models' if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model and vectorizer
joblib.dump(clf, "models/model.pkl")
joblib.dump(vec, "models/vectorizer.pkl")

print("Model and vectorizer saved in 'models/'")


