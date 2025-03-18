'''
recommendation_model.py
'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# === Load Dataset ===
file_path = os.path.join("data", "cleaned_sneaker_data.csv")
df = pd.read_csv(file_path)

# Combine relevant text-based features (brand, name, colorway, silhouette)
df['combined_features'] = (
    df['Brand'] + " " + df['Name'] + " " +
    df['Colorway'] + " " + df['Silhouette']
).fillna('')

# === Vectorize & Compute Similarity Matrix ===
vectorizer = TfidfVectorizer(stop_words='english')
feature_matrix = vectorizer.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(feature_matrix)

print("Recommendation Model Ready: TF-IDF Matrix:", feature_matrix.shape)

# === Recommendation Function ===
def get_recommendations(Brand, Colorway, Max_price, Silhouette, Gender, df, cosine_sim, top_n=5):
    df['Brand'] = df['Brand'].str.lower()
    df['Colorway'] = df['Colorway'].str.lower()
    df['Silhouette'] = df['Silhouette'].str.lower()
    df['Gender'] = df['Gender'].str.lower()

    brand = Brand.lower().strip() if Brand else ""
    colorway = Colorway.lower().strip() if Colorway else ""
    silhouette = Silhouette.lower().strip() if Silhouette else ""
    gender = Gender.lower().strip() if Gender else ""

    df['Retail Price'] = pd.to_numeric(df['Retail Price'], errors='coerce')

    # === Dynamic filtering ===
    filter_conditions = (df['Retail Price'] <= Max_price)

    if brand:
        filter_conditions &= (df['Brand'] == brand)

    if colorway:
        filter_conditions &= (df['Colorway'].str.contains(colorway, case=False, na=False))

    if gender:
        filter_conditions &= (df['Gender'] == gender)

    filtered_df = df[filter_conditions]

    if filtered_df.empty:
        return pd.DataFrame()

    item_index = filtered_df.index[0]
    sim_scores = list(enumerate(cosine_sim[item_index]))

    # --- BOOST silhouette matches ---
    boosted_scores = []
    for idx, score in sim_scores:
        candidate = df.iloc[idx]
        boost = 0.30 if silhouette and candidate['Silhouette'] == silhouette else 0  # boost for matching silhouette
        boosted_scores.append((idx, score + boost))

    # Sort after boosting
    boosted_scores = sorted(boosted_scores, key=lambda x: x[1], reverse=True)

    # Collect top_n results regardless of silhouette
    recommended_indices = [idx for idx, _ in boosted_scores[1:top_n + 1]]  # skip self

    return df.iloc[recommended_indices] if recommended_indices else pd.DataFrame()
