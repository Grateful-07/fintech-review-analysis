import os
import logging
import pandas as pd
from sqlalchemy import create_engine, text

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Update credentials as needed (or set via environment variable)
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "bank_reviews")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_engine():
    return create_engine(DATABASE_URL)

def run_schema_file():
    """Applies schema.sql to initialize tables."""
    engine = get_engine()
    if os.path.exists("schema.sql"):
        with open("schema.sql", "r") as f:
            sql_script = f.read()
        with engine.connect() as conn:
            conn.execute(text(sql_script))
            conn.commit()
        logging.info("Applied schema.sql successfully.")

def save_processed_reviews(df: pd.DataFrame):
    """Maps and inserts cleaned reviews into PostgreSQL."""
    engine = get_engine()
    
    # Map bank_name to bank_id
    banks_df = pd.read_sql("SELECT bank_id, bank_name FROM banks", con=engine)
    df_merged = df.merge(banks_df, left_on="bank", right_on="bank_name")
    
    # Rename columns to match PostgreSQL schema
    db_df = df_merged.rename(columns={
        "review": "review_text",
        "date": "review_date"
    })
    
    db_df["source"] = "Google Play Store"
    
    # Target columns
    columns = ["bank_id", "review_text", "rating", "review_date", "sentiment_label", "sentiment_score", "identified_theme", "source"]
    final_db_df = db_df[columns]
    
    final_db_df.to_sql("reviews", con=engine, if_exists="append", index=False)
    logging.info(f"Successfully inserted {len(final_db_df)} review records into PostgreSQL database '{DB_NAME}'.")

def verify_data():
    """Runs verification queries."""
    engine = get_engine()
    with engine.connect() as conn:
        res = conn.execute(text("""
            SELECT b.bank_name, COUNT(r.review_id) as total_reviews, ROUND(AVG(r.rating), 2) as avg_rating
            FROM banks b
            LEFT JOIN reviews r ON b.bank_id = r.bank_id
            GROUP BY b.bank_name;
        """))
        print("\n--- DATA VERIFICATION RESULTS ---")
        for row in res:
            print(f"Bank: {row[0]} | Reviews: {row[1]} | Avg Rating: {row[2]} ?")
