import joblib

MODEL_PATH = "models/spam_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def predict_spam(text: str):
    model, vectorizer = load_model()
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return bool(prediction)