# Email Spam Classifier using NLP and Linear SVM

A simple and effective **email spam classifier** built using Natural Language Processing (NLP) and a **Linear Support Vector Machine (SVM)**.  
This project includes full data preprocessing, feature extraction using TF-IDF, model training, evaluation, visualization, and a ready-to-use prediction function.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [File Structure](#file-structure)
- [License](#license)

---

## Project Overview
This project implements a pipeline to classify emails as **HAM (legitimate)** or **SPAM (unwanted)**:

1. **Text Preprocessing**
   - Remove email addresses, URLs, phone numbers, punctuation, and stopwords  
   - Lemmatization using spaCy  
   - Preserve important spam-indicating words like "free", "win", "money", etc.  

2. **Feature Extraction**
   - TF-IDF Vectorization with unigrams and bigrams  
   - Vocabulary limited to top 10,000 features  

3. **Model Training**
   - Linear Support Vector Classifier (`LinearSVC`)  
   - Handles class imbalance automatically with `class_weight='balanced'`  

4. **Evaluation**
   - Accuracy, Precision, Recall, F1-Score  
   - Confusion matrix, error analysis, and visualization of performance metrics  

5. **Prediction**
   - Ready-to-use function `predict_email_spam()` to classify new emails  

---

## Dataset
The dataset contains emails labeled as **HAM (0)** or **SPAM (1)**.  

- Original CSV: `Dataset/emails.csv`  
- Cleaned CSV after removing duplicates: `Dataset/emails_cleaned.csv`  

> Note: Do not include large datasets in GitHub if sensitive; you can provide instructions for users to download it separately.

---

## Features
- Email preprocessing using **regex** and **spaCy**  
- Custom stopwords list with important spam words preserved  
- TF-IDF vectorization with unigrams and bigrams  
- Linear SVM classifier for robust spam detection  
- Detailed evaluation and visualizations using **matplotlib** and **seaborn**  
- Prediction function saved for reuse without retraining  

---

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier
