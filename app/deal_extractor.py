from app.utils import clean_text
import re


def extract_product(text: str):
    text = clean_text(text)

    text = re.sub(r'[\$₹]\s?\d+', '', text)
    text = re.sub(r'\d+%', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    stopwords = [
        "get", "on", "for", "with", "and", "the", "a",
        "now", "only", "discount", "offer", "sale", "limited"
    ]

    words = text.split()
    product_words = [w for w in words if w not in stopwords and len(w) > 1]

    return " ".join(product_words).strip()


def extract_deals(text: str):
    deals = []

    price_pattern = r'[\$₹]\s?\d+'
    discount_pattern = r'\d+%'

    prices = re.findall(price_pattern, text)
    discounts = re.findall(discount_pattern, text)

    product = extract_product(text)

    if prices or discounts:
        deals.append({
            "product": product,
            "prices": prices,
            "discounts": discounts
        })

    return deals