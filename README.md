# 📨 Email Spam Classifier using NLP & Linear SVM

A **high-accuracy spam email classification system** using **Natural Language Processing** and **Linear Support Vector Machine**. Achieves **99%+ accuracy** in distinguishing between legitimate (HAM) and unwanted (SPAM) emails.

---

## 🚀 Key Features

- ✅ **Custom Email Preprocessing Pipeline** - Removes headers, URLs, phone numbers, excessive whitespace
- ✅ **Smart Stopword Handling** - Preserves important spam indicators like `free`, `win`, `money`, `urgent`
- ✅ **Advanced TF-IDF Vectorization** - Unigrams + bigrams with 10K feature vocabulary
- ✅ **Optimized Linear SVM** - Balanced class weights for imbalanced datasets
- ✅ **Stratified Data Splitting** - Maintains real-world spam/ham distribution
- ✅ **Comprehensive Evaluation Suite** - Precision, recall, F1-score, confusion matrix
- ✅ **Interactive Visualizations** - Performance metrics, error analysis, confidence distribution
- ✅ **Production-Ready Model Persistence** - Save/load with joblib

---

## 📊 Dataset & Performance

**Dataset Requirements:**
- CSV format with `text` (email content) and `spam` (0=HAM, 1=SPAM) columns
- Typical size: 5,000+ emails for reliable training
- Natural class imbalance supported (e.g., 76% HAM, 24% SPAM)

**Expected Performance:**
- **Accuracy:** 95-99%
- **Precision (SPAM):** >95% (minimal false positives)
- **Recall (SPAM):** >90% (catches most spam)
- **Training Time:** <30 seconds on modern hardware

---

## 🛠️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP.git
cd Email-Spam-Classifier
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the Notebook
```bash
jupyter notebook notebooks/spam_classifier_notebook.ipynb
```

---

## 📂 Project Structure

```
Email-Spam-Classifier/
├── Dataset/
│   └── emails.csv                    # Training dataset
├── notebooks/
│   └── Email_Spam_Classification_Using_NLP.ipynb   # Main implementation
├── saved_models/
│   └── spam_classifier_model.joblib     # Trained model
├── requirements.txt                  # Python dependencies
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

---

## 🔧 Model Architecture

```
Email Text → Custom Preprocessing → TF-IDF Vectorization → Linear SVM → HAM/SPAM
```

**Pipeline Components:**
1. **Preprocessing:** Remove emails, URLs, phone numbers, normalize text
2. **Tokenization:** spaCy lemmatization with custom stopwords
3. **Vectorization:** TF-IDF with unigrams+bigrams (max 10K features)
4. **Classification:** LinearSVC with balanced class weights

**Key Parameters:**
- `max_features=10000` - Vocabulary size limit
- `ngram_range=(1,2)` - Unigrams and bigrams
- `class_weight='balanced'` - Handle imbalanced data
- `random_state=42` - Reproducible results

---

## 🎯 Usage Examples

### Training the Model
```python
# Load and preprocess data
data_spam = pd.read_csv('Dataset/emails.csv')
X_train, X_test, y_train, y_test = train_test_split(
    data_spam['text'], data_spam['spam'], 
    test_size=0.2, stratify=data_spam['spam']
)

# Train pipeline
spam_classifier_pipeline.fit(X_train, y_train)

# Evaluate
accuracy = spam_classifier_pipeline.score(X_test, y_test)
print(f"Accuracy: {accuracy:.3f}")
```

### Making Predictions
```python
import joblib

# Load trained model
model = joblib.load('saved_models/spam_classifier_model.joblib')

# Predict single email
email = "Congratulations! You won $1000! Click here to claim now!"
prediction = model.predict([email])[0]
confidence = model.decision_function([email])[0]

print(f"Prediction: {'SPAM' if prediction==1 else 'HAM'}")
print(f"Confidence: {confidence:.2f}")
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
    print(f"{'SPAM' if pred==1 else 'HAM'}: {email[:30]}...")
```

---

## 📈 Evaluation Metrics

The model provides comprehensive evaluation:

- **Accuracy Score** - Overall correctness
- **Classification Report** - Per-class precision, recall, F1-score
- **Confusion Matrix** - Detailed error breakdown
- **ROC Analysis** - Performance visualization
- **Sample Predictions** - Real examples with confidence scores

**Critical Metrics for Spam Detection:**
- **False Positives (HAM→SPAM):** Critical to minimize - legitimate emails marked as spam
- **False Negatives (SPAM→HAM):** Less critical but still important - spam reaching inbox

---

## 📊 Visualizations

The notebook generates 6 key visualizations:
1. **Confusion Matrix Heatmap** - Classification accuracy breakdown
2. **Performance Metrics Bar Chart** - HAM vs SPAM metrics comparison
3. **Prediction Confidence Distribution** - Model certainty levels
4. **Class Distribution Comparison** - Actual vs predicted balance
5. **Error Analysis Breakdown** - Types of classification errors
6. **Performance Summary Dashboard** - Key metrics overview

---

## 🚀 Deployment Options

- **Local Inference:** Direct prediction using saved pipeline
- **Web API:** Deploy with Flask/FastAPI for real-time classification
- **Email Server Integration:** Filter emails at server level
- **Batch Processing:** Classify large email volumes efficiently

---

## 🔧 Customization

**Improve Performance:**
```python
# Experiment with different algorithms
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

# Adjust TF-IDF parameters
tfidf = TfidfVectorizer(
    max_features=20000,     # Increase vocabulary
    ngram_range=(1,3),      # Add trigrams
    min_df=3,               # More restrictive filtering
)

# Add email-specific features
# - Sender reputation
# - HTML content ratio
# - Email length statistics
```

---

## 📋 Requirements

**Python Version:** 3.8+

**Core Dependencies:**
- `scikit-learn` - Machine learning algorithms
- `spacy` - Natural language processing
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `seaborn` - Statistical visualization
- `joblib` - Model persistence

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Heshan Ranasinghe**  
Electronic & Telecommunication Engineering Undergraduate

- 🌐 GitHub: [@DPHeshanRanasinghe](https://github.com/DPHeshanRanasinghe)
- 📧 Email: hranasinghe505@gmail.com
- 💼 LinkedIn: [Connect with me](https://github.com/DPHeshanRanasinghe/Email-Spam-Classification-using-NLP)

---

## 🙏 Acknowledgments

- [scikit-learn](https://scikit-learn.org/) for machine learning tools
- [spaCy](https://spacy.io/) for NLP capabilities
- [Jupyter](https://jupyter.org/) for interactive development environment
- Email spam research community for domain insights

---

## 📚 References & Further Reading

- [TF-IDF Vectorization Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [Linear SVM Documentation](https://scikit-learn.org/stable/modules/svm.html#svm-classification)
- [Email Spam Filtering Techniques](https://en.wikipedia.org/wiki/Email_filtering)
- [NLP Best Practices for Text Classification](https://developers.google.com/machine-learning/guides/text-classification)
