# Email Spam Classifier using NLP and Linear SVM

A simple and effective **email spam classifier** built using **Natural Language Processing (NLP)** and a **Linear Support Vector Machine (SVM)**.  
This project implements a complete workflow: data preprocessing, feature extraction using TF-IDF, model training, evaluation, visualization, and ready-to-use prediction functions.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Preprocessing and Cleaning](#preprocessing-and-cleaning)
4. [Feature Extraction](#feature-extraction)
5. [Model Training](#model-training)
6. [Model Evaluation](#model-evaluation)
7. [Prediction](#prediction)
8. [Visualizations](#visualizations)
9. [Installation](#installation)
10. [Usage](#usage)
11. [File Structure](#file-structure)
12. [Best Practices](#best-practices)
13. [License](#license)

---

## Project Overview
This project classifies emails into **HAM (legitimate)** and **SPAM (unwanted)**.  
The main steps include:

1. **Data cleaning** – remove email headers, URLs, punctuation, numbers, and stopwords. Preserve important spam words like "free", "win", "money", etc.  
2. **Feature extraction** – convert cleaned emails into TF-IDF vectors using unigrams and bigrams.  
3. **Classification** – train a **Linear SVM** classifier, optimized for imbalanced data using `class_weight='balanced'`.  
4. **Evaluation** – calculate accuracy, precision, recall, F1-score, and generate confusion matrices.  
5. **Prediction** – provide a reusable function to classify new emails.  

This pipeline ensures a **robust spam detection system** ready for real-world applications.

---

## Dataset
The dataset is a collection of emails labeled as **HAM (0)** or **SPAM (1)**:

- Original CSV: `Dataset/emails.csv`  
- Cleaned CSV (duplicates removed): `Dataset/emails_cleaned.csv`  

### Dataset Statistics
- Total emails: varies depending on dataset  
- Class distribution: ~HAM/Spam ratio preserved via stratified splitting  
- Email lengths and word counts are analyzed for preprocessing purposes  

> **Note:** Large datasets should not be pushed to GitHub. You can provide instructions to download them separately.

---

## Preprocessing and Cleaning
Email text is preprocessed with the following steps:

1. Remove email addresses, URLs, phone numbers, and excessive whitespace using **regular expressions**.  
2. Tokenization and **lemmatization** using **spaCy** (`en_core_web_sm`).  
3. Removal of **punctuation, numbers, very short tokens (<3 characters)**.  
4. Custom stopword list:
   - Standard English stopwords (from spaCy)  
   - Email-specific stopwords: `'email', 'mail', 'send', 'subject', 'dear', 'hello', 'hi', 'regards'`  
   - Spam-important words preserved: `'free', 'win', 'money', 'urgent', 'limited', 'offer', 'now', 'only', 'today'`  

This ensures the **classifier focuses on relevant tokens** for spam detection.

---

## Feature Extraction
- **TF-IDF Vectorization**
  - Converts emails into numerical features  
  - Includes **unigrams and bigrams**  
  - Maximum of **10,000 features** for efficiency  
  - Terms appearing in fewer than 2 documents or more than 95% of emails are ignored  
- Stopwords are removed during tokenization, so `stop_words=None` in TF-IDF  

---

## Model Training
- **Classifier:** `LinearSVC` (Linear Support Vector Machine)  
- Handles class imbalance with `class_weight='balanced'`  
- Maximum iterations increased to 10,000 (`max_iter=10000`) to ensure convergence  
- Pipeline steps:
  1. TF-IDF vectorization  
  2. Linear SVM classification  

Training split uses **stratified 80-20 split** to preserve class ratio.

---

## Model Evaluation
The trained model is evaluated using:

1. **Accuracy**
2. **Precision, Recall, F1-Score** (class-wise and averaged)  
3. **Confusion Matrix** with:
   - True Negatives (HAM→HAM)  
   - False Positives (HAM→SPAM) – Important emails misclassified  
   - False Negatives (SPAM→HAM) – Spam in inbox  
   - True Positives (SPAM→SPAM)  

Example metrics:

| Class  | Precision | Recall | F1-Score |
|--------|-----------|--------|----------|
| HAM    | 0.99      | 0.98   | 0.99     |
| SPAM   | 0.98      | 0.99   | 0.98     |

---

## Prediction
The saved model pipeline can be used to classify new emails:

```python
from saved_models.spam_classifier_model_<timestamp>_predict_function import predict_email_spam

email_text = "Congratulations! You won a free iPhone. Click here now!"
result = predict_email_spam(email_text)

print(result)
# Output:
# {
#   'prediction': 'SPAM',
#   'confidence_score': 2.45,
#   'is_spam': True
# }
