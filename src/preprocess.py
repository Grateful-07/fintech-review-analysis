import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def preprocess_reviews(df: pd.DataFrame) -> pd.DataFrame:
    initial_len = len(df)
    
    # Drop rows missing essential text or rating
    df = df.dropna(subset=['review', 'rating']).copy()
    df['review'] = df['review'].astype(str).str.strip()
    df = df[df['review'] != ""]
    
    # Deduplicate reviews
    if 'review_id' in df.columns:
        df = df.drop_duplicates(subset=['review_id'])
    df = df.drop_duplicates(subset=['review', 'bank'])
    
    # Standardize date to YYYY-MM-DD
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    cols = ['review_id', 'review', 'rating', 'date', 'bank', 'source']
    df = df[[c for c in cols if c in df.columns]]
    
    logging.info(f"Preprocessing finished: Dropped {initial_len - len(df)} rows. Final count: {len(df)}.")
    return df
