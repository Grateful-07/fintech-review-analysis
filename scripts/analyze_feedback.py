import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

THEME_KEYWORDS = {
    "Transaction Performance": ["slow", "transfer", "delay", "loading", "waiting", "speed", "pending", "network"],
    "Account Access & Security": ["login", "error", "otp", "password", "sign in", "fingerprint", "biometric", "locked"],
    "UI & User Experience": ["interface", "ui", "design", "beautiful", "confusing", "navigation", "clean", "update"],
    "Customer Support": ["help", "support", "chat", "bot", "call", "agent", "service", "complain"]
}

def assign_theme(review_text):
    if not isinstance(review_text, str):
        return "General Feedback"
    review_lower = review_text.lower()
    for theme, keywords in THEME_KEYWORDS.items():
        for keyword in keywords:
            if keyword in review_lower:
                return theme
    return "General Feedback"

def analyze_sentiment_and_themes():
    input_file = 'data/raw/cleaned_reviews.csv'
    output_file = 'data/raw/analyzed_reviews.csv'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Run the scraping script first!")
        return

    print("Loading cleaned dataset...")
    df = pd.read_csv(input_file)
    
    print("Running Sentiment Analysis...")
    analyzer = SentimentIntensityAnalyzer()
    sentiment_labels = []
    sentiment_scores = []
    
    for text in df['review']:
        if pd.isna(text):
            sentiment_labels.append("neutral")
            sentiment_scores.append(0.0)
            continue
        score = analyzer.polarity_scores(str(text))['compound']
        sentiment_scores.append(score)
        if score >= 0.05:
            sentiment_labels.append("positive")
        elif score <= -0.05:
            sentiment_labels.append("negative")
        else:
            sentiment_labels.append("neutral")
            
    df['sentiment_label'] = sentiment_labels
    df['sentiment_score'] = sentiment_scores
    
    print("Extracting business themes...")
    df['identified_theme'] = df['review'].apply(assign_theme)
    df.insert(0, 'review_id', range(1, len(df) + 1))
    
    df.to_csv(output_file, index=False)
    print(f"\n? Saved analyzed dataset to: {output_file}")

if __name__ == "__main__":
    analyze_sentiment_and_themes()
