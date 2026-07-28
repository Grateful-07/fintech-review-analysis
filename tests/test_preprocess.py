import pandas as pd
from src.preprocess import preprocess_reviews

def test_preprocessing_removes_duplicates_and_nulls():
    raw_data = pd.DataFrame([
        {"review_id": "1", "review": "Super smooth app", "rating": 5, "date": "2026-05-10", "bank": "CBE", "source": "Google Play"},
        {"review_id": "1", "review": "Super smooth app", "rating": 5, "date": "2026-05-10", "bank": "CBE", "source": "Google Play"},
        {"review_id": "2", "review": None, "rating": 1, "date": "2026-05-11", "bank": "BOA", "source": "Google Play"},
        {"review_id": "3", "review": "Login timeout error", "rating": 2, "date": "2026-05-12", "bank": "Dashen", "source": "Google Play"}
    ])
    
    cleaned = preprocess_reviews(raw_data)
    assert len(cleaned) == 2
    assert "date" in cleaned.columns
