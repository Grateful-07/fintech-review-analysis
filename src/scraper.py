import logging
from typing import Dict
import pandas as pd
from google_play_scraper import Sort, reviews

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

BANK_APP_MAPPING: Dict[str, str] = {
    "CBE": "com.cbe.cbebirr",
    "BOA": "com.boa.boamay",
    "Dashen": "com.dashen.mbanking"
}

def scrape_bank_reviews(bank_name: str, app_id: str, count: int = 500) -> pd.DataFrame:
    logging.info(f"Scraping reviews for {bank_name} ({app_id})...")
    try:
        scraped, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=count
        )
        data = []
        for item in scraped:
            data.append({
                "review_id": item.get("reviewId"),
                "review": item.get("content"),
                "rating": item.get("score"),
                "date": item.get("at"),
                "bank": bank_name,
                "source": "Google Play"
            })
        df = pd.DataFrame(data)
        logging.info(f"Retrieved {len(df)} reviews for {bank_name}.")
        return df
    except Exception as e:
        logging.error(f"Error scraping {bank_name}: {e}")
        return pd.DataFrame()

def collect_all_reviews(target_count: int = 500) -> pd.DataFrame:
    frames = []
    for bank, app_id in BANK_APP_MAPPING.items():
        df = scrape_bank_reviews(bank, app_id, count=target_count)
        if not df.empty:
            frames.append(df)
    if not frames:
        raise RuntimeError("No reviews collected across configured app IDs.")
    return pd.concat(frames, ignore_index=True)
