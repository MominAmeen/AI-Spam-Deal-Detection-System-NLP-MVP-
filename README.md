# AI Spam & Deal Detection System (NLP MVP)

## Overview

This project is an AI-powered text processing system that classifies messages as spam or legitimate content and extracts valuable deal information from unstructured text. It is designed as a Minimum Viable Product (MVP) to demonstrate real-world NLP applications in filtering noise and identifying actionable offers from emails and notifications.

---

## Features

* Spam vs Non-Spam Classification using Machine Learning
* Extraction of Deals (Product, Price, Discount)
* Product Identification from Unstructured Text
* REST API built with FastAPI
* Real-time Text Analysis

---

## Tech Stack

* Python
* Scikit-learn (TF-IDF, Naive Bayes)
* FastAPI
* Regex-based Text Processing

---

## Project Structure

```
ai-spam-deal-detector/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── deal_extractor.py
│   ├── utils.py
│
├── train/
│   └── train_model.py
│
├── data/
│   └── spam.csv
│
├── models/
│   └── spam_model.pkl
│
├── requirements.txt
├── README.md
├── .gitignore
```

---

## API Endpoint

### POST /analyze

#### Input

```json
{
  "text": "Limited offer! Get 40% discount on car tires for $80"
}
```

#### Output

```json
{
  "status": "success",
  "spam": false,
  "deal_count": 1,
  "deals": [
    {
      "product": "car tires",
      "prices": ["$80"],
      "discounts": ["40%"]
    }
  ]
}
```

---

## How to Run

```bash
pip install -r requirements.txt
python train/train_model.py
uvicorn app.main:app --reload
```

## Future Improvements

* Advanced NLP models (Transformers/BERT)
* Smart deal ranking and filtering
* User-based query support (e.g., "under $100")
* Integration with email/notification APIs

---

## Author

Developed as an AI/ML project demonstrating practical NLP and backend integration.
