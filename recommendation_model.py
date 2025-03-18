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

    # === Build dynamic filter ===
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

    # Use first matching sneaker as reference for cosine similarity
    item_index = filtered_df.index[0]
    sim_scores = list(enumerate(cosine_sim[item_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommended_indices = []
    i = 1

    while len(recommended_indices) < top_n and i < len(sim_scores):
        idx = sim_scores[i][0]
        candidate = df.iloc[idx]

        silhouette_ok = (not silhouette) or (candidate['Silhouette'] == silhouette)
        gender_ok = (not gender) or (candidate['Gender'] == gender)

        if silhouette_ok and gender_ok:
            recommended_indices.append(idx)

        i += 1

    return df.iloc[recommended_indices] if recommended_indices else pd.DataFrame()

