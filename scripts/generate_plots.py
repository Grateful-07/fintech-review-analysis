import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visual_plots():
    db_file = 'data/bank_reviews.db'
    if not os.path.exists(db_file):
        print(f"Error: {db_file} not found!")
        return

    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("""
        SELECT b.bank_name, r.sentiment_label, r.identified_theme 
        FROM reviews r 
        JOIN banks b ON r.bank_id=b.bank_id
    """, conn)
    conn.close()

    sns.set_theme(style='whitegrid')

    # Chart 1: Sentiment Profile Matrix
    plt.figure(figsize=(10, 6))
    pd.crosstab(df['bank_name'], df['sentiment_label'], normalize='index').plot(
        kind='bar', stacked=True, color=['#e74c3c', '#95a5a6', '#2ecc71']
    )
    plt.title('Customer Sentiment Distribution: Ethiopian Fintech Apps (2026)', fontsize=12, fontweight='bold')
    plt.ylabel('Proportion')
    plt.tight_layout()
    plt.savefig('data/sentiment_distribution.png', dpi=300)
    plt.close()

    # Chart 2: Operational Issue Clusters
    plt.figure(figsize=(10, 6))
    filtered_df = df[df['identified_theme'] != 'General Feedback']
    sns.countplot(data=filtered_df, y='identified_theme', hue='bank_name', palette='Blues_d')
    plt.title('Operational Feedback Clusters by Bank App', fontsize=12, fontweight='bold')
    plt.xlabel('Volume of Reviews')
    plt.ylabel('Thematic Category')
    plt.tight_layout()
    plt.savefig('data/theme_frequencies.png', dpi=300)
    plt.close()

    print('\n✅ Visual analytics charts beautifully generated in the data/ folder!')

if __name__ == '__main__':
    generate_visual_plots()
