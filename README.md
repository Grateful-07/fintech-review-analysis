# Ethiopian Fintech Analytics: End-to-End Consumer Feedback Pipeline

A production-grade data engineering and NLP intelligence pipeline that harvests, transforms, analyzes, and models user feedback for major Ethiopian mobile banking applications (**CBE Birr**, **BOA Live**, and **Dashen Amole**).

## 🚀 System Architecture

The pipeline processes consumer metrics through four cleanly separated functional modules:
1. **Data Ingestion (`scrape_reviews.py`)**: Connects to the Google Play Store tracking engine with built-in fallback protocols to guarantee dataset generation.
2. **NLP Sentiment Analytics (`analyze_feedback.py`)**: Utilizes the VADER sentiment algorithm to map emotional indicators and labels text into operational business categories.
3. **Relational Database Modeling (`setup_database.py`)**: Normalizes flat datasets and inserts them into an ACID-compliant SQLite relational database schema utilizing primary and foreign key constraints.
4. **Data Visualization Engine (`generate_plots.py`)**: Extracts metrics directly from the SQL database using complex relational queries to compile charts.

## 📂 Project Structure
```text
fintech-review-analytics/
├── data/                       # Local data directory (Git ignored binaries)
│   ├── raw/
│   │   ├── cleaned_reviews.csv
│   │   └── analyzed_reviews.csv
│   ├── bank_reviews.db        # Relational SQL Database
│   ├── sentiment_distribution.png
│   └── theme_frequencies.png
├── scripts/                    # Clean modular source scripts
│   ├── scrape_reviews.py
│   ├── analyze_feedback.py
│   ├── setup_database.py
│   └── generate_plots.py
├── .gitignore                  # Keeps raw data out of your commit logs
├── requirements.txt            # System dependencies
└── README.md                   # Project documentation