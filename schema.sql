-- PostgreSQL Schema for Fintech Review Analytics

DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS banks;

-- Banks Table
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(50) UNIQUE NOT NULL,
    app_name VARCHAR(100) NOT NULL
);

-- Reviews Table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id) ON DELETE CASCADE,
    review_text TEXT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_date TIMESTAMP,
    sentiment_label VARCHAR(20),
    sentiment_score NUMERIC(5, 4),
    identified_theme VARCHAR(100),
    source VARCHAR(50) DEFAULT 'Google Play Store'
);

-- Populate Default Bank Metadata
INSERT INTO banks (bank_name, app_name) VALUES
('CBE', 'com.combanketh.mobilebanking'),
('BOA', 'com.boa.boaMobileBanking'),
('Dashen', 'com.dashen.dashensuperapp');
