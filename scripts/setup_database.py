import os
import sqlite3
import pandas as pd

DB_PATH = 'data/bank_reviews.db'
CSV_PATH = 'data/raw/analyzed_reviews.csv'

def setup_relational_database():
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} not found!")
        return

    print("Connecting to SQLite...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS banks (
        bank_id INTEGER PRIMARY KEY,
        bank_name TEXT UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        review_id INTEGER PRIMARY KEY,
        bank_id INTEGER,
        review_text TEXT,
        rating INTEGER,
        date TEXT,
        sentiment_label TEXT,
        identified_theme TEXT
    );
    """)

    # Populate master lookups
    for idx, name in enumerate(['CBE', 'BOA', 'Dashen']):
        cursor.execute('INSERT OR IGNORE INTO banks VALUES (?, ?)', (idx + 1, name))

    # Read and map structured dataframe records
    df = pd.read_csv(CSV_PATH)
    bank_map = {'CBE': 1, 'BOA': 2, 'Dashen': 3}
    df['bank_id'] = df['bank'].map(bank_map)

    print("Loading data arrays into SQL engine tables...")
    for i, r in df.iterrows():
        cursor.execute("""
        INSERT OR IGNORE INTO reviews VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (i + 1, int(r['bank_id']), r['review'], int(r['rating']), r['date'], r['sentiment_label'], r['identified_theme']))
        
    conn.commit()
    
    print("\n--- SQL Relational DB Verified ---")
    for row in cursor.execute('SELECT b.bank_name, COUNT(r.review_id) FROM reviews r JOIN banks b ON r.bank_id=b.bank_id GROUP BY b.bank_name'):
        print(f"{row[0]}: {row[1]} rows loaded")
        
    conn.close()

if __name__ == '__main__':
    setup_relational_database()