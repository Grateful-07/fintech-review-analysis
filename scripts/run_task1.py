import os
import logging
from src.scraper import collect_all_reviews
from src.preprocess import preprocess_reviews

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    os.makedirs("data/raw", exist_ok=True)
    
    logging.info("Starting Task 1: Web Scraping...")
    raw_df = collect_all_reviews(target_count=500)
    
    logging.info("Starting Task 1: Preprocessing...")
    clean_df = preprocess_reviews(raw_df)
    
    output_path = "data/raw/cleaned_reviews.csv"
    clean_df.to_csv(output_path, index=False)
    logging.info(f"Task 1 Complete! Cleaned data saved to {output_path} ({len(clean_df)} reviews).")

if __name__ == "__main__":
    main()
