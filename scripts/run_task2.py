import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
import pandas as pd
from src.sentiment_thematic import analyze_sentiment, run_thematic_pipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    input_path = "data/raw/cleaned_reviews.csv"
    if not os.path.exists(input_path):
        raise FileNotFoundError("Cleaned dataset not found in data/raw/cleaned_reviews.csv. Run scripts/run_task1.py first.")
        
    logging.info(f"Loading cleaned dataset from {input_path}...")
    df = pd.read_csv(input_path)
    
    logging.info("Running Task 2: Sentiment Analysis...")
    df_sentiment = analyze_sentiment(df)
    
    logging.info("Running Task 2: Thematic Categorization...")
    final_df = run_thematic_pipeline(df_sentiment)
    
    output_path = "data/processed_reviews.csv"
    final_df.to_csv(output_path, index=False)
    logging.info(f"Task 2 Complete! Output saved to {output_path} ({len(final_df)} processed rows).")

if __name__ == "__main__":
    main()
