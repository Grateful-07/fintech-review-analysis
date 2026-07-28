import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
os.makedirs("reports/figures", exist_ok=True)

df = pd.read_csv("data/processed_reviews.csv")

# 1. Sentiment Distribution by Bank
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x="bank", hue="sentiment_label", palette={"POSITIVE": "#2ecc71", "NEGATIVE": "#e74c3c", "NEUTRAL": "#95a5a6"})
plt.title("Sentiment Distribution across Ethiopian Banking Apps", fontsize=14, fontweight='bold')
plt.xlabel("Bank", fontsize=12)
plt.ylabel("Number of Reviews", fontsize=12)
plt.tight_layout()
plt.savefig("reports/figures/sentiment_distribution.png", dpi=300)
plt.close()

# 2. Rating Distribution per Bank
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="bank", y="rating", palette="Set2")
plt.title("Rating Distribution per Bank", fontsize=14, fontweight='bold')
plt.xlabel("Bank", fontsize=12)
plt.ylabel("Rating (1-5 ?)", fontsize=12)
plt.tight_layout()
plt.savefig("reports/figures/rating_distribution.png", dpi=300)
plt.close()

# 3. Theme Frequency per Bank
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y="identified_theme", hue="bank", palette="Blues_r")
plt.title("Dominant Customer Themes & Pain Points", fontsize=14, fontweight='bold')
plt.xlabel("Review Count", fontsize=12)
plt.ylabel("Identified Theme", fontsize=12)
plt.tight_layout()
plt.savefig("reports/figures/theme_frequency.png", dpi=300)
plt.close()

print("Task 4 figures successfully generated in 'reports/figures/'!")
