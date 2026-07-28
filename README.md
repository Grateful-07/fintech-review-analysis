Set-Content -Path "README.md" -Value @"
# Fintech Review Analytics Pipeline

An end-to-end data engineering and analytics pipeline designed to scrape, clean, analyze, and store Google Play Store customer reviews for major Ethiopian commercial banks: **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**.

---

## 📌 Project Overview

This project provides actionable insights into mobile banking app performance and customer sentiment by categorizing feedback into key operational themes such as **Account Access**, **System Performance**, **UI/UX**, and **Customer Support**.

### Key Features
* **Automated Data Scraper (`google-play-scraper`)**: Dynamically fetches up to 500 latest customer reviews for CBE, BOA, and Dashen Bank.
* **Text Preprocessing & Cleaning**: Standardizes text, removes noise, and handles missing/duplicate entries.
* **Sentiment Analysis Engine**: Leverages VADER NLP lexicon for fast, reliable positive/negative sentiment and polarity scoring.
* **Thematic Analysis & Keyword Mining**: Maps reviews into predefined banking pain points using rule-based keyword matching and TF-IDF n-grams.
* **Modular Codebase**: Organized package structure with separated modules for scraping, processing, running scripts, and unit testing (`pytest`).

---

## 📁 Repository Structure

```text
fintech-review-analytics/
├── data/
│   ├── raw/                  # Cleaned raw output (cleaned_reviews.csv)
│   └── processed_reviews.csv # Final processed data with sentiment & themes
├── src/
│   ├── scraper.py            # Google Play Store scraping logic
│   ├── preprocess.py         # Text normalization and cleaning functions
│   └── sentiment_thematic.py # VADER sentiment engine & theme classification
├── scripts/
│   ├── run_task1.py          # Pipeline execution for Task 1 (Scrape & Clean)
│   └── run_task2.py          # Pipeline execution for Task 2 (Sentiment & Themes)
├── tests/
│   ├── test_preprocess.py    # Unit tests for preprocessing
│   └── test_sentiment.py     # Unit tests for thematic mapping
├── .gitignore
├── README.md
└── requirements.txt