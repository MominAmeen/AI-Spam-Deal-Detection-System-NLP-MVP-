import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    return text.strip()


def extract_numbers(text: str):
    return re.findall(r'\d+', text)