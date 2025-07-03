# 💼 Freelancer Job Analysis & Intelligent Recommendation System

This project offers a comprehensive solution for analyzing freelance job markets and assisting freelancers in finding suitable opportunities using advanced machine learning techniques. It consists of **three major components**:

---

## 📊 1. Job Clustering & Market Analysis

We applied **unsupervised learning** to group thousands of job postings into meaningful **job clusters** using natural language features from job titles and descriptions.

### 🔍 Key Features:
- Extracted textual features and embedded them using Word2Vec.
- Applied clustering to detect hidden job categories based on skills and descriptions.
- Analyzed the clusters across:
  - 🌍 Countries
  - ⏰ Time patterns (day, month, hour)
  - 💰 Hourly vs Fixed-price jobs
  - 💵 Salary ranges

### 📈 Visualization:
- Interactive plots using Plotly for exploring:
  - Most common clusters
  - Distribution of job types
  - Country-specific demand
  - Temporal trends and salary averages

---

## 🤖 2. Recommendation System

An **intelligent recommender system** that suggests the most relevant jobs based on the freelancer's skillset.

### 🛠️ How it Works:
- Users select their skills from a predefined list.
- Each skill is mapped using a pre-trained **Word2Vec model**.
- The system computes a **cosine similarity** score between the freelancer's skill vector and all job vectors.
- Jobs with the highest similarity scores are recommended.

### 🎯 Output:
- Top 10 most similar jobs with their descriptions and similarity scores.
- Visualized similarity scores using interactive bar charts.

---

## 🧠 3. Job Type Classification (Hourly vs Fixed-Price)

A supervised ML model that classifies whether a job is **hourly** or **fixed-price** based on its title and description.

### ⚙️ Pipeline:
- Preprocessed text using TF-IDF vectorization.
- Trained a **Logistic Regression** model.
- Achieved high accuracy in distinguishing between job types.

### 🧪 Features:
- Real-time prediction of job type from user input.
- Confidence score shown alongside the prediction.

---

## 🧰 Technologies Used

- `Python`, `Pandas`, `NumPy`
- `Word2Vec`, `scikit-learn`, `TF-IDF`
- `Plotly`, `Matplotlib`, `Seaborn`
- `Streamlit` for full-stack interactive deployment

---

## 📌 Project Highlights

- Combined unsupervised and supervised ML techniques in one unified app.
- Full interactive interface with **multi-page navigation** in Streamlit.
- All models pre-trained and saved for optimized performance.

## Note:
- The files of data and app is on my account drive.
- In ``notebook NLP & Clustring`` you should dowenload it to view this.
