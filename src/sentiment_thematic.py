import logging
from typing import List, Tuple
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Download VADER lexicon (tiny, ~100KB)
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

THEME_RULES = {
    "Account Access & Authentication": ["login", "otp", "password", "pin", "biometric", "fingerprint", "sign in", "register", "lock", "access"],
    "Transaction & System Performance": ["slow", "crash", "transfer", "failed", "pending", "error", "loading", "network", "stuck", "timeout"],
    "UI & User Experience": ["interface", "design", "easy", "clean", "simple", "ux", "ui", "update", "look"],
    "Customer Support & Reliability": ["service", "support", "branch", "call", "help", "agent", "money deducted", "refund"]
}

def analyze_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """Fast, offline sentiment analysis using VADER."""
    logging.info("Running VADER sentiment analysis...")
    sia = SentimentIntensityAnalyzer()
    
    labels, scores = [], []
    for text in df['review'].fillna(''):
        compound = sia.polarity_scores(str(text))['compound']
        scores.append(round(abs(compound), 4))
        if compound >= 0.05:
            labels.append("POSITIVE")
        elif compound <= -0.05:
            labels.append("NEGATIVE")
        else:
            labels.append("NEUTRAL")
            
    df['sentiment_label'] = labels
    df['sentiment_score'] = scores
    return df

def assign_theme(text: str) -> str:
    text_lower = str(text).lower()
    for theme, keywords in THEME_RULES.items():
        if any(kw in text_lower for kw in keywords):
            return theme
    return "General Feedback"

def extract_top_tfidf_ngrams(reviews: List[str], top_n: int = 10) -> List[Tuple[str, float]]:
    if not reviews:
        return []
    vectorizer = TfidfVectorizer(ngram_range=(2, 3), stop_words='english', max_features=100)
    tfidf_matrix = vectorizer.fit_transform(reviews)
    feature_names = vectorizer.get_feature_names_out()
    sums = tfidf_matrix.sum(axis=0)
    
    data = [(feature_names[idx], sums[0, col]) for col, idx in enumerate(range(len(feature_names)))]
    ranking = sorted(data, key=lambda x: x[1], reverse=True)
    return ranking[:top_n]

def run_thematic_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Extracting business themes from review text...")
    df['identified_theme'] = df['review'].apply(assign_theme)
    return df
