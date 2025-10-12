from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# Initialize FastAPI
app = FastAPI(title="Book Genre Classifier API")

# Load model and vectorizer
model_path = "models/model.pkl"
vectorizer_path = "models/vectorizer.pkl"

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    raise FileNotFoundError("Model or vectorizer not found. Run classify.py first.")

clf = joblib.load(model_path)
vec = joblib.load(vectorizer_path)

# Define input schema
class Book(BaseModel):
    title: str

# Define routes
@app.get("/")
def home():
    return {"message": "Welcome to the Book Genre Classifier API!"}

@app.post("/predict/")
def predict(book: Book):
    X = vec.transform([book.title])
    prediction = clf.predict(X)[0]
    return {"title": book.title, "predicted_label": prediction}

