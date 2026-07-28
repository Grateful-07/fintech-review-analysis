import logging
import pandas as pd
from google_play_scraper import reviews, Sort

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Target apps on Google Play Store
APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

def fetch_reviews_for_app(app_name: str, app_id: str, target_count: int = 500) -> pd.DataFrame:
    """Scrapes up to target_count reviews for a single Google Play app."""
    logging.info(f"Scraping reviews for {app_name} ({app_id})...")
    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=target_count
        )
        
        if not result:
            logging.warning(f"No reviews returned for {app_name}. Checking fallback query...")
            return pd.DataFrame()

        df = pd.DataFrame(result)
        df['bank'] = app_name
        df['app_id'] = app_id
        
        # Standardize minimal required columns
        columns_map = {
            'content': 'review',
            'score': 'rating',
            'at': 'date',
            'userName': 'user_name'
        }
        df = df.rename(columns=columns_map)
        logging.info(f"Retrieved {len(df)} reviews for {app_name}.")
        return df[['bank', 'app_id', 'review', 'rating', 'date', 'user_name']]

    except Exception as e:
        logging.error(f"Error scraping {app_name} ({app_id}): {e}")
        return pd.DataFrame()

def collect_all_reviews(target_count: int = 500) -> pd.DataFrame:
    """Collects reviews across all configured banking apps into a single DataFrame."""
    all_dfs = []
    for app_name, app_id in APPS.items():
        df = fetch_reviews_for_app(app_name, app_id, target_count=target_count)
        if not df.empty:
            all_dfs.append(df)

    if not all_dfs:
        raise RuntimeError("No reviews collected across configured app IDs. Check network connectivity or package IDs.")

    combined_df = pd.concat(all_dfs, ignore_index=True)
    return combined_df
