
# Ethiopian Fintech Review Analytics Pipeline

An end-to-end data engineering and analytics pipeline designed to scrape, clean, analyze, persistently store, and visualize customer reviews from the Google Play Store for commercial banking apps in Ethiopia: **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**.

---

## 📌 Executive Summary

This repository contains a production-ready data pipeline that transforms unstructured play store customer feedback into actionable fintech insights. By combining fast rule-based sentiment analysis, TF-IDF n-gram keyword mining, relational PostgreSQL persistence, and interactive visualization dashboards, this project equips product teams with data-backed recommendations to resolve critical app pain points.

---

## 📂 Repository Architecture & Structure

```text
fintech-review-analysis/
├── data/
│   ├── raw/                      # Cleaned raw scrapings (cleaned_reviews.csv)
│   └── processed_reviews.csv     # Task 2 dataset with sentiment & business themes
├── reports/
│   └── figures/                  # Publication-ready task 4 chart exports
│       ├── sentiment_distribution.png
│       ├── rating_distribution.png
│       └── theme_frequency.png
├── src/
│   ├── scraper.py                # Task 1: Google Play Store scraping logic
│   ├── preprocess.py             # Task 1: Text cleaning & normalization engine
│   ├── sentiment_thematic.py     # Task 2: VADER sentiment & thematic analyzer
│   └── database.py               # Task 3: PostgreSQL schema & ingestion pipeline
├── scripts/
│   ├── run_task1.py              # Scrapes & cleans play store reviews
│   ├── run_task2.py              # Executes sentiment & theme extraction
│   ├── run_task3.py              # Initializes schema & populates PostgreSQL
│   └── run_task4_visuals.py      # Generates analytical figures for reporting
├── tests/
│   ├── test_preprocess.py        # Pytest unit testing for text processing
│   └── test_sentiment.py         # Pytest unit testing for thematic rules
├── app.py                        # Streamlit interactive analytics dashboard
├── schema.sql                    # PostgreSQL relational database DDL
├── requirements.txt              # Project dependencies
└── README.md                     # Full pipeline documentation
