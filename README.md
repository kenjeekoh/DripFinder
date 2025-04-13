# DripFinder 👟  
**AI-Powered Sneaker Picks, No Cap**

DripFinder is an intelligent sneaker recommendation system built with NLP and interactive UI technologies to help sneakerheads discover the perfect pair. Whether you're into Jordans, Yeezys, or classic NBs, DripFinder curates sneaker recommendations based on your personal style, price preferences, and color vibes.  

## 🔍 Project Overview

Sneaker shopping can be overwhelming with thousands of releases, colorways, and resellers. DripFinder solves this by using a personalized recommendation engine that combines:

- User-inputted style preferences (brand, silhouette, colors, budget)
- NLP-based similarity matching
- A custom Streamlit-powered web app for easy exploration  

The result? Instant sneaker picks tailored to your exact taste.

---

## 📦 Dataset

- **Source**: The Sneaker Database API + Web scraping (e.g., StockX links)
- **Size**: ~2000+ sneaker entries across top brands: Nike, Jordan, adidas, Puma, New Balance
- **Features**:
  - Sneaker Name
  - Brand
  - Retail Price & Estimated Market Value
  - Colorway
  - Silhouette
  - Purchase Link
  - Release Date

---

## 🧠 Methodology

### 1. **Data Cleaning & Expansion**
- Filled missing values, normalized brand/silhouette names
- Expanded underrepresented silhouettes via API queries
- Fetched dynamic market data from public resale sources

### 2. **NLP Recommendation Engine**
- Vectorized sneaker attributes using TF-IDF
- Used **Cosine Similarity** to rank sneakers based on user preferences
- Applied filters for price ceilings and colorway matches

### 3. **User Interface (Streamlit)**
- Multipage layout for:
  - Profile Check-In (name, gender/age)
  - Preference Form (brand, silhouette, colorway, price)
  - Final Recommendations (with images and purchase links)
- Dynamic dropdowns, auto-updating silhouette options per brand

---

## 🚀 Key Features

- ✅ **Personalized**: Tailors results by brand, silhouette, budget, and colorway
- 🎨 **Interactive UI**: Streamlit interface with dropdowns, tag selectors, and real-time results
- 🤖 **NLP-Powered**: Recommender system built using TF-IDF + cosine similarity
- 💸 **Market-Savvy**: Integrates resale value to help users gauge sneaker worth

---

## 📊 Results & Performance

- Achieved accurate style-based matching on test queries
- Dynamic filtering ensured top 5 most relevant sneaker results for user inputs
- System scalability confirmed by processing >2k sneakers within milliseconds per query

---

## 🛠️ Technical Stack

- **Python** (pandas, numpy, scikit-learn, requests, re)
- **Streamlit** (for interactive web app)
- **NLP Tools**: TF-IDF Vectorizer, Cosine Similarity
- **API Integration**: TheSneakerDB API + Custom scraping scripts

---

## 🧑‍💻 Installation & Usage

```bash
# Clone the repo
git clone https://github.com/kenjeekoh/DripFinder.git
cd DripFinder

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run Home.py
