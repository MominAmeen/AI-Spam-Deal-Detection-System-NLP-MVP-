from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_spam
from app.deal_extractor import extract_deals

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/analyze")
def analyze(data: InputText):
    spam = predict_spam(data.text)

    if spam:
        return {"spam": True, "deals": []}

    deals = extract_deals(data.text)

    return {
    "spam": False,
    "deal_count": len(deals),
    "deals": deals
}