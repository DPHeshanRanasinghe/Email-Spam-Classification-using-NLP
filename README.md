# Email Spam Classification using Natural Language Processing

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![spaCy](https://img.shields.io/badge/spaCy-3.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Accuracy](https://img.shields.io/badge/accuracy-99.4%25-brightgreen.svg)
![Status](https://img.shields.io/badge/status-production--ready-success.svg)

A machine learning-based email spam classifier implementing Natural Language Processing techniques to distinguish between spam and legitimate emails. The system achieves 99.4% accuracy using LinearSVC with TF-IDF vectorization and custom text preprocessing pipeline.

## Performance Metrics

- **Accuracy**: 99.4%
- **ROC-AUC Score**: 0.9997
- **Precision/Recall**: Balanced performance across both classes
- **False Positive Rate**: Minimal (optimized for legitimate email preservation)

## Key Features

- Custom text preprocessing pipeline with regex-based cleaning
- Lemmatization and stopword removal using spaCy
- TF-IDF vectorization with unigram and bigram features
- LinearSVC classifier with class balancing
- Comprehensive evaluation with confusion matrix and feature importance
- Timestamp-based model versioning for deployment tracking

## Technical Stack

- **Language**: Python 3.7+
- **ML Framework**: scikit-learn
- **NLP Library**: spaCy (en_core_web_sm)
- **Visualization**: Matplotlib, Seaborn, WordCloud
- **Model Persistence**: Joblib, Pickle

## Project Structure

```
Email-Spam-Classifier/
├── Email_Spam_Classification_Using_NLP.ipynb
├── spam_classifier_model_<timestamp>.joblib
├── spam_classifier_model_<timestamp>.pkl
├── spam_classifier_model_<timestamp>_metadata.json
├── spam_classifier_model_<timestamp>_predict_function.py
├── Dataset/
│   ├── emails.csv
│   └── emails_cleaned.csv
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier
```

Install dependencies:
```bash
pip install pandas numpy scikit-learn spacy matplotlib seaborn wordcloud joblib
python -m spacy download en_core_web_sm
```

## Usage

### Training the Model

Launch Jupyter Notebook:
```bash
jupyter notebook Email_Spam_Classification_Using_NLP.ipynb
```

Execute cells sequentially:
1. Data loading and exploration
2. Text preprocessing and cleaning
3. Feature extraction (TF-IDF)
4. Model training and evaluation
5. Model saving with metadata

### Making Predictions

Use the generated prediction function:
```python
from spam_classifier_model_<timestamp>_predict_function import predict_email_spam

# Classify a new email
email_text = "Congratulations! You've won a free vacation. Click here now!"
result = predict_email_spam(email_text, model_path="spam_classifier_model_<timestamp>.joblib")

print(f"Classification: {result['prediction']}")
print(f"Confidence: {result['confidence']:.2f}%")
```

## Data Preprocessing Pipeline

### Text Cleaning Steps
1. Email address removal
2. URL and hyperlink removal
3. Phone number removal
4. Excessive whitespace normalization
5. Lowercasing

### NLP Processing
1. Tokenization using spaCy
2. Lemmatization
3. Stopword removal (custom list)
4. Spam-indicator word preservation

## Model Architecture

```
Raw Email Text
    ↓
Text Cleaning (Regex)
    ↓
spaCy Processing (Lemmatization)
    ↓
TF-IDF Vectorization (1-2 grams)
    ↓
LinearSVC Classifier
    ↓
Spam/Ham Classification
```

**Model Configuration:**
- Vectorizer: TF-IDF (max_features=3000, ngram_range=(1,2))
- Classifier: LinearSVC (class_weight='balanced')
- Train/Test Split: 80/20 (stratified)

## Results

### Classification Performance

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 99.4%  |
| Precision | 99.3%  |
| Recall    | 99.5%  |
| F1-Score  | 99.4%  |
| ROC-AUC   | 0.9997 |

### Feature Importance

**Top Spam Indicators:**
- click, now, life, http, man, low, software

**Top Ham Indicators:**
- vince, enron, thank, research, model, energy

### Error Analysis
- Minimal false positives (important emails marked as spam)
- Low false negative rate (spam emails passing through)
- Model performs consistently across email lengths

## Deployment Recommendations

### Production Considerations
1. **Monitoring**: Track false positive rates to avoid blocking legitimate emails
2. **User Feedback**: Implement correction mechanism for misclassifications
3. **Model Retraining**: Schedule periodic retraining with new data
4. **Confidence Thresholds**: Adjust classification thresholds based on business requirements
5. **A/B Testing**: Validate model performance before full deployment

### Scalability
- Model size: ~5MB (efficient for production)
- Inference time: <10ms per email
- Batch processing supported

## Future Enhancements

- Deep learning models (LSTM, BERT) for improved context understanding
- Multi-language support
- Real-time streaming classification
- Integration with email clients (API development)
- Explainable AI features (LIME/SHAP)

## Dataset

The model is trained on a balanced dataset containing:
- Spam emails: Marketing, phishing, scam content
- Ham emails: Legitimate business and personal correspondence

**Note**: Ensure compliance with data privacy regulations when deploying with real email data.

## Contributing

Contributions are welcome. Please follow these steps:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -m 'Add enhancement'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Submit Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## References

- [scikit-learn Documentation](https://scikit-learn.org/)
- [spaCy NLP Library](https://spacy.io/)
- [TF-IDF Vectorization](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

## Author

**Your Name**  
Your Title/Department

- Email: your.email@example.com
- GitHub: [DPHeshanRanasinghe](https://github.com/DPHeshanRanasinghe)
- LinkedIn: [Heshan Ranasinghe](https://www.linkedin.com/in/heshan-ranasinghe-988b00290/)

## Citation

```bibtex
@software{heshan2025spamclassifier,
  author = {Heshan Ranasinghe},
  title = {Email Spam Classification using Natural Language Processing},
  year = {2025},
  url = {https://github.com/DPHeshanRanasinghe/email-spam-classifier}
}
```