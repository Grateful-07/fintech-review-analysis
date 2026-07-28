import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
import pandas as pd
from src.database import run_schema_file, save_processed_reviews, verify_data

def main():
    input_path = "data/processed_reviews.csv"
    if not os.path.exists(input_path):
        raise FileNotFoundError("data/processed_reviews.csv not found. Run Task 1 and 2 first.")
    
    df = pd.read_csv(input_path)
    print("Setting up PostgreSQL schema...")
    run_schema_file()
    
    print("Inserting records...")
    save_processed_reviews(df)
    
    print("Executing verification queries...")
    verify_data()

if __name__ == "__main__":
    main()
