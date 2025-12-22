# Email Spam Classification using NLP

## Overview
This project implements an end-to-end email spam classifier using Natural Language Processing (NLP) techniques and machine learning. The solution leverages a Linear Support Vector Machine (LinearSVC) with TF-IDF vectorization and custom text preprocessing to accurately distinguish between spam and legitimate (ham) emails.

## Features
- **Data Cleaning & Preprocessing:**
  - Removal of email addresses, URLs, phone numbers, and excessive whitespace
  - Lemmatization and stopword removal using spaCy
  - Custom stopword list tailored for email content
  - Preservation of important spam-indicator words
- **Exploratory Data Analysis:**
  - Distribution analysis of spam vs ham
  - Email length and word count statistics
  - Word cloud visualizations for both classes
- **Model Pipeline:**
  - TF-IDF vectorization (unigrams & bigrams)
  - LinearSVC classifier with class balancing
  - Stratified train-test split for robust evaluation
- **Performance Evaluation:**
  - Accuracy, precision, recall, F1-score, ROC-AUC
  - Confusion matrix and error analysis
  - Feature importance analysis (top spam/ham indicator words)
- **Model Saving & Deployment:**
  - Model and metadata saved with timestamp
  - Standalone prediction function for deployment

## Project Structure
```
Email_Spam_Classification_Using_NLP.ipynb   # Main Jupyter notebook (full workflow)
spam_classifier_model_<timestamp>.joblib     # Trained model (Joblib format)
spam_classifier_model_<timestamp>.pkl        # Model backup (Pickle format)
spam_classifier_model_<timestamp>_metadata.json  # Model metadata
spam_classifier_model_<timestamp>_predict_function.py # Standalone prediction function
Dataset/
    emails.csv                              # Raw email dataset
    emails_cleaned.csv                      # Cleaned dataset
```

## How to Run
1. **Install Requirements:**
   - Python 3.7+
   - Install dependencies:
     ```bash
     pip install pandas numpy scikit-learn spacy matplotlib seaborn wordcloud joblib
     python -m spacy download en_core_web_sm
     ```
2. **Open the Notebook:**
   - Launch `Email_Spam_Classification_Using_NLP.ipynb` in Jupyter or VS Code.
3. **Run All Cells:**
   - The notebook is organized step-by-step: data loading, cleaning, EDA, model training, evaluation, and saving.
4. **Model Output:**
   - Trained model, metadata, and prediction function are saved with a timestamp for easy deployment.

## Prediction Function Usage
You can use the generated Python function to classify new emails:
```python
from spam_classifier_model_<timestamp>_predict_function import predict_email_spam
result = predict_email_spam("Your email text here", model_path="spam_classifier_model_<timestamp>.joblib")
print(result)
```

## Key Results
- **Accuracy:** ~99.4%
- **ROC-AUC:** ~0.9997 (Excellent)
- **Top Spam Indicators:** click, now, life, http, man, low, software
- **Top Ham Indicators:** vince, enron, thank, research, model, energy

## Recommendations for Deployment
- Monitor false positives (important emails marked as spam)
- Implement user feedback for continuous improvement
- Retrain regularly with new data
- Consider A/B testing and confidence thresholds

## License
This project is for educational and research purposes. Please cite appropriately if used in publications.
