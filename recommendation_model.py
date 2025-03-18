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

    silhouette = Silhouette.lower().strip() if Silhouette else ""
    gender = Gender.lower().strip() if Gender else ""

    df['Retail Price'] = pd.to_numeric(df['Retail Price'], errors='coerce')

    filtered_df = df[
        (df['Brand'] == Brand.lower()) &
        (df['Colorway'].str.contains(Colorway.lower(), case=False, na=False)) &
        (df['Retail Price'] <= Max_price)
    ]

    if gender:
        filtered_df = filtered_df[filtered_df['Gender'] == gender]

    if filtered_df.empty:
        return pd.DataFrame()

    item_index = filtered_df.index[0]
    sim_scores = list(enumerate(cosine_sim[item_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommended_indices = []
    i = 1

    while len(recommended_indices) < top_n and i < len(sim_scores):
        idx = sim_scores[i][0]
        candidate = df.iloc[idx]

        silhouette_match = silhouette and candidate['Silhouette'] == silhouette
        silhouette_ok = (not silhouette) or silhouette_match

        gender_match = gender and candidate['Gender'] == gender
        gender_ok = (not gender) or gender_match

        if silhouette_ok and gender_ok:
            recommended_indices.append(idx)

        i += 1

    return df.iloc[recommended_indices] if recommended_indices else pd.DataFrame()
