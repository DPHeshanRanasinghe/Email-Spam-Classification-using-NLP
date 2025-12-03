# 📧 Email Spam Classification Using NLP

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Machine Learning](https://img.shields.io/badge/ML-Spam%20Detection-green.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-99.39%25-brightgreen.svg)
![ROC-AUC](https://img.shields.io/badge/ROC--AUC-0.9997-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A state-of-the-art email spam classification system using **Natural Language Processing (NLP)** and **Machine Learning**. This project achieves **99.39% accuracy** with a **0.9997 ROC-AUC score** using Linear SVM and TF-IDF vectorization.

---

## 🎯 Project Overview

This project implements an advanced spam email classifier that can distinguish between legitimate (HAM) and spam emails with exceptional accuracy. The system uses sophisticated NLP techniques including spaCy lemmatization, custom text preprocessing, and TF-IDF feature extraction combined with a Linear Support Vector Machine classifier.

### ✨ Key Features

- ✅ **99.39% Accuracy** on test set (1,139 emails)
- ✅ **ROC-AUC Score: 0.9997** (Excellent discrimination ability)
- ✅ **Advanced Text Preprocessing** with spaCy NLP
- ✅ **Custom Email Cleaning** (removes URLs, emails, phone numbers)
- ✅ **Feature Importance Analysis** (identifies key spam indicators)
- ✅ **Comprehensive Visualizations** (word clouds, ROC curves, confusion matrices)
- ✅ **Production-Ready** with saved model artifacts
- ✅ **Smart Stopword Handling** - Preserves spam indicators like `free`, `win`, `money`

---

## 📊 Performance Metrics

| Metric | HAM (Legitimate) | SPAM (Unwanted) | Overall |
|--------|------------------|-----------------|---------|
| **Precision** | 99.65% | 98.55% | 99.39% |
| **Recall** | 99.54% | 98.91% | 99.39% |
| **F1-Score** | 0.9960 | 0.9872 | 0.9938 |

### 📈 Confusion Matrix Analysis

| Actual ↓ / Predicted → | HAM | SPAM |
|------------------------|-----|------|
| **HAM** | 861 ✅ | 4 ❌ |
| **SPAM** | 3 ❌ | 271 ✅ |

- **True Negatives**: 861 (HAM correctly classified)
- **True Positives**: 271 (SPAM correctly detected)
- **False Positives**: 4 (HAM marked as SPAM) ⚠️
- **False Negatives**: 3 (SPAM marked as HAM)

### 📦 Dataset Information

- **Total Emails**: 5,728 raw → 5,695 after removing 33 duplicates
- **HAM Emails**: 4,327 (76.0%)
- **SPAM Emails**: 1,368 (24.0%)
- **Training Set**: 4,556 emails (80%)
- **Test Set**: 1,139 emails (20%)
- **Training Time**: ~3 minutes on standard hardware

---

## 🛠️ Technologies Used

### Core Libraries
- **Python 3.8+**
- **scikit-learn** - Machine Learning algorithms
- **spaCy** (en_core_web_sm) - Advanced NLP and text preprocessing
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **matplotlib & seaborn** - Data visualization
- **wordcloud** - Word cloud generation
- **joblib** - Model persistence

### Machine Learning Pipeline
- **Algorithm**: Linear Support Vector Machine (LinearSVC)
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Feature Engineering**: Unigrams + Bigrams (1-2 grams)
- **Vocabulary Size**: 10,000 features
- **Class Balancing**: Enabled for imbalanced dataset

---

## 🚀 Installation & Setup

### Prerequisites
```bash
# Python 3.8 or higher
python --version
```

### Step 1: Clone the Repository
```bash
git clone https://github.com/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP.git
cd Email-Spam-Classification-using-NLP
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

---

## 📝 Usage

### Option 1: Run the Jupyter Notebook
```bash
jupyter notebook Email_Spam_Classification_Using_NLP.ipynb
```

### Option 2: Use the Trained Model

```python
import joblib

# Load the trained model
model = joblib.load('spam_classifier_model_<timestamp>.joblib')

# Predict on new email
email_text = "Congratulations! You've won $1,000,000! Click here now!"
prediction = model.predict([email_text])[0]
confidence = model.decision_function([email_text])[0]

print(f"Prediction: {'SPAM' if prediction == 1 else 'HAM'}")
print(f"Confidence Score: {confidence:.4f}")
```

### Option 3: Use the Prediction Function
```python
from spam_classifier_model_<timestamp>_predict_function import predict_email_spam

# Predict spam
result = predict_email_spam("Your email text here")
print(result)
# Output: {'prediction': 'SPAM', 'confidence_score': 2.5432, 'is_spam': True}
```

### Batch Predictions
```python
# Predict multiple emails
emails = [
    "Meeting scheduled for 3 PM today",
    "FREE MONEY! Act now, limited time!",
    "Please review the attached document"
]

predictions = model.predict(emails)
for email, pred in zip(emails, predictions):
    label = 'SPAM' if pred == 1 else 'HAM'
    print(f"{label}: {email[:50]}...")
```

---

## 🗂️ Project Structure

```
Email-Spam-Classification-using-NLP/
│
├── Email_Spam_Classification_Using_NLP.ipynb  # Main Jupyter notebook
├── Dataset/
│   ├── emails.csv                              # Original dataset
│   └── emails_cleaned.csv                      # Cleaned dataset (duplicates removed)
│
├── spam_classifier_model_<timestamp>.joblib    # Trained model (joblib format)
├── spam_classifier_model_<timestamp>.pkl       # Trained model (pickle format)
├── spam_classifier_model_<timestamp>_metadata.json  # Model metadata
├── spam_classifier_model_<timestamp>_predict_function.py  # Prediction helper
│
├── requirements.txt                            # Project dependencies
├── .gitignore                                  # Git ignore rules
└── README.md                                   # Project documentation
```

---

## 🔍 Model Pipeline Architecture

```
┌─────────────────┐
│  Raw Email Text │
└────────┬────────┘
         ↓
┌─────────────────────────┐
│  Text Preprocessing     │
│  • Remove email addrs   │
│  • Remove URLs          │
│  • Remove phone numbers │
│  • Remove whitespace    │
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│  spaCy NLP Processing   │
│  • Tokenization         │
│  • Lemmatization        │
│  • Stopword removal     │
│    (335 custom)         │
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│  TF-IDF Vectorization   │
│  • Unigrams + Bigrams   │
│  • 10,000 max features  │
│  • Min df=2, Max df=0.95│
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│  Linear SVM Classifier  │
│  • Balanced weights     │
│  • C=1.0                │
│  • Max iter=10,000      │
└────────┬────────────────┘
         ↓
┌─────────────────────────┐
│  Prediction & Confidence│
│  HAM (0) or SPAM (1)    │
└─────────────────────────┘
```

---

## 🔬 Key Technical Details

### 1. Custom Email Preprocessing
```python
def clean_email_text(text):
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    # Remove phone numbers
    text = re.sub(r'\d{3}[-.]?\d{3}[-.]?\d{4}', '', text)
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # spaCy lemmatization
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc 
              if not token.is_stop and token.is_alpha]
    
    return ' '.join(tokens)
```

### 2. Smart Stopword Management
- **Total Stopwords**: 335 custom + spaCy defaults
- **Preserved Spam Indicators**: `free`, `win`, `money`, `urgent`, `click`, `offer`
- **Reason**: These words are strong spam signals and removing them would hurt accuracy

### 3. TF-IDF Configuration
```python
TfidfVectorizer(
    preprocessor=clean_email_text,  # Custom preprocessing
    max_features=10000,              # Vocabulary size
    ngram_range=(1, 2),              # Unigrams + bigrams
    min_df=2,                        # Min document frequency
    max_df=0.95,                     # Max document frequency
    strip_accents='unicode',
    lowercase=True
)
```

### 4. Linear SVM Parameters
```python
LinearSVC(
    class_weight='balanced',  # Handle imbalanced dataset
    C=1.0,                    # Regularization parameter
    max_iter=10000,           # Maximum iterations
    random_state=42           # Reproducibility
)
```

---

## 📈 Feature Importance Analysis

### Top 20 SPAM Indicator Words
`click`, `now`, `life`, `http`, `man`, `low`, `software`, `account`, `love`, `free`, `site`, `die`, `sex`, `online`, `sell`, `death`, `money`, `viagra`, `learn`, `spam`

### Top 20 HAM Indicator Words
`vince`, `enron`, `thank`, `research`, `model`, `energy`, `password`, `kaminski`, `option`, `attach`, `question`, `let know`, `subscription`, `pdf`, `houston`, `pjm`, `doc`, `enron com`, `risk`, `shirley`

**Insight**: The model correctly identifies business-specific terms (company names, professional vocabulary) as HAM indicators and promotional/suspicious terms as SPAM indicators.

---

## 📊 Comprehensive Visualizations

The notebook includes 8+ visualization types:

1. **📊 Data Distribution Analysis**
   - Email count distributions (HAM vs SPAM)
   - Text length distributions
   - Word count distributions
   - Box plots for statistical comparison

2. **☁️ Word Clouds**
   - Most common words in HAM emails
   - Most common words in SPAM emails
   - Visual pattern recognition

3. **🎯 Model Performance**
   - Confusion matrix heatmap
   - Precision, Recall, F1-Score bar charts
   - ROC curve with AUC=0.9997
   - Prediction confidence distribution

4. **🔍 Feature Importance**
   - Top 20 SPAM indicator coefficients
   - Top 20 HAM indicator coefficients
   - Feature weight visualization

5. **📈 Final Summary Report**
   - Comprehensive performance dashboard
   - Key metrics overview
   - Error analysis

---

## 🎓 Methodology & Approach

### Phase 1: Data Exploration
- Analyzed 5,728 raw emails
- Identified and removed 33 duplicates
- Examined class distribution (76% HAM, 24% SPAM)
- Analyzed text length and word count patterns

### Phase 2: Preprocessing Pipeline
- Created custom `clean_email_text()` function
- Integrated spaCy for advanced NLP
- Removed email-specific noise (URLs, addresses, phone numbers)
- Applied lemmatization for word normalization
- Curated 335 custom stopwords (preserved spam indicators)

### Phase 3: Feature Engineering
- Implemented TF-IDF vectorization
- Used unigrams + bigrams for richer features
- Limited vocabulary to 10,000 most informative features
- Applied min/max document frequency filtering

### Phase 4: Model Training
- Selected Linear SVM for speed and interpretability
- Applied balanced class weights for imbalanced data
- Used stratified train-test split (80-20)
- Training completed in ~3 minutes

### Phase 5: Evaluation & Analysis
- Comprehensive metrics: Accuracy, Precision, Recall, F1, ROC-AUC
- Confusion matrix for error analysis
- Feature importance extraction
- Confidence score distribution analysis
- Generated visualizations for insights

---

## 🚀 Deployment Recommendations

### Production Checklist
- ✅ **Model Artifacts**: Saved in multiple formats (.joblib, .pkl)
- ✅ **Metadata**: Training parameters and statistics stored
- ✅ **Prediction Function**: Ready-to-use Python function provided
- ✅ **Performance**: Sub-second inference time
- ✅ **Reliability**: 99.39% accuracy on test set

### Deployment Options

1. **REST API Integration**
```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('spam_classifier_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.json['email']
    prediction = model.predict([email_text])[0]
    confidence = model.decision_function([email_text])[0]
    
    return jsonify({
        'is_spam': bool(prediction),
        'confidence': float(confidence)
    })
```

2. **Email Server Integration**
   - Filter emails at SMTP/IMAP level
   - Quarantine high-confidence spam
   - Flag suspicious emails for review

3. **Batch Processing**
   - Process large volumes efficiently
   - Generate daily/weekly spam reports
   - Monitor spam trends over time

4. **Real-time Classification**
   - Integrate with email clients
   - Instant spam detection
   - User feedback loop

### Best Practices

1. **Monitor False Positives** ⚠️
   - Track legitimate emails marked as spam
   - Implement user feedback mechanism
   - Regularly review misclassifications

2. **Regular Model Updates**
   - Retrain monthly with new spam patterns
   - Incorporate user feedback
   - Monitor performance drift

3. **Confidence Thresholds**
   - High confidence (>2.0): Auto-move to spam
   - Medium confidence (0.5-2.0): Flag for review
   - Low confidence (<0.5): Keep in inbox

4. **A/B Testing**
   - Test different classification thresholds
   - Compare model versions
   - Measure user satisfaction

5. **Logging & Monitoring**
   - Track prediction distributions
   - Monitor model latency
   - Detect data drift

---

## 📦 Model Artifacts

The trained model is saved in multiple formats:

| File | Size | Purpose |
|------|------|---------|
| `*.joblib` | ~0.42 MB | Primary model (recommended) |
| `*.pkl` | ~0.42 MB | Pickle backup |
| `*_metadata.json` | ~2 KB | Training info, metrics, parameters |
| `*_predict_function.py` | ~3 KB | Ready-to-use prediction function |
| `emails_cleaned.csv` | Variable | Deduplicated dataset |

---

## 🔧 Requirements

Create a `requirements.txt` file with:

```txt
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
spacy>=3.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
wordcloud>=1.8.0
jupyter>=1.0.0
joblib>=1.0.0
```

Install spaCy language model:
```bash
python -m spacy download en_core_web_sm
```

---

## 🤝 Contributing

Contributions are welcome! Here are ways to contribute:

### Areas for Enhancement

1. **Model Improvements**
   - Implement ensemble methods (Random Forest, XGBoost)
   - Add deep learning models (LSTM, BERT, Transformers)
   - Hyperparameter tuning with GridSearchCV

2. **Feature Engineering**
   - Add sender reputation features
   - Include HTML/plain text ratio
   - Extract email metadata (headers, attachments)
   - Analyze email structure patterns

3. **User Interface**
   - Create web demo with Flask/Streamlit
   - Build Chrome extension for Gmail
   - Develop desktop email client plugin

4. **Advanced Features**
   - Multi-language support
   - Phishing detection
   - Malicious link detection
   - Image-based spam detection

5. **Performance Optimization**
   - Model quantization for mobile
   - ONNX export for cross-platform
   - GPU acceleration for batch processing

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**D.P. Heshan Ranasinghe**  
*Electronic & Telecommunication Engineering Undergraduate*

- 🌐 GitHub: [@DPHeshanRanasinghe](https://github.com/DPHeshanRanasinghe)
- 📧 Email: hranasinghe505@gmail.com
- 💼 LinkedIn: [Heshan Ranasinghe](https://www.linkedin.com/in/heshan-ranasinghe-988b00290)
- 📂 Repository: [Email-Spam-Classification-using-NLP](https://github.com/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP)

---

## 🙏 Acknowledgments

- **spaCy Team** - Excellent NLP library and language models
- **scikit-learn Contributors** - Robust machine learning tools
- **Email Dataset Providers** - Training data for the model
- **Open Source Community** - Inspiration and support

---

## 📚 References & Further Reading

### Documentation
- [scikit-learn: TF-IDF Vectorization](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [scikit-learn: Linear SVM](https://scikit-learn.org/stable/modules/svm.html#svm-classification)
- [spaCy: Industrial-Strength NLP](https://spacy.io/usage/spacy-101)

### Research Papers
- [A Survey of Machine Learning Techniques for Spam Filtering](https://www.researchgate.net/publication/220433908_A_survey_of_machine_learning_techniques_for_spam_filtering)
- [Text Classification using SVM](https://ieeexplore.ieee.org/document/7839876)

### Articles & Tutorials
- [Email Spam Filtering Techniques](https://en.wikipedia.org/wiki/Email_filtering)
- [NLP Best Practices for Text Classification](https://developers.google.com/machine-learning/guides/text-classification)
- [Handling Imbalanced Datasets](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)

---

## 📞 Support

If you have questions or need help:

1. 📖 Check the [Issues](https://github.com/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP/issues) page
2. 🐛 Open a new issue with detailed description
3. ⭐ Star the repository if you found it helpful!
4. 🔄 Fork and contribute improvements

---

## 🎯 Project Status

| Status | Description |
|--------|-------------|
| ✅ **Production Ready** | Model trained and validated |
| ✅ **Documentation Complete** | Comprehensive README and code comments |
| ✅ **Artifacts Saved** | Multiple model formats available |
| ✅ **Tested** | 99.39% accuracy on holdout test set |
| 🚀 **Ready for Deployment** | All components operational |

---

## 📊 Quick Stats

```
⏱️ Training Time: ~3 minutes
📈 Accuracy: 99.39%
🎯 ROC-AUC: 0.9997
📧 Dataset: 5,695 emails
🔢 Features: 10,000 TF-IDF
✅ Test Accuracy: 1,132/1,139 correct
❌ Misclassifications: Only 7 errors
```

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

**Built with ❤️ using Python, scikit-learn, and spaCy**

[![GitHub stars](https://img.shields.io/github/stars/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP?style=social)](https://github.com/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP?style=social)](https://github.com/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP/network/members)

</div>
