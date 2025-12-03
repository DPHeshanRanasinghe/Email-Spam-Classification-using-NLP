
import joblib

def predict_email_spam(email_text, model_path="spam_classifier_model_20251203_062849.joblib"):
    """
    Predict if an email is spam or ham.

    Args:
        email_text (str): The email content to classify
        model_path (str): Path to the saved model

    Returns:
        dict: Prediction result with confidence score
    """
    try:
        # Load the trained model
        model = joblib.load(model_path)

        # Make prediction
        prediction = model.predict([email_text])[0]
        confidence = model.decision_function([email_text])[0]

        return {
            'prediction': 'SPAM' if prediction == 1 else 'HAM',
            'confidence_score': float(confidence),
            'is_spam': bool(prediction)
        }
    except Exception as e:
        return {'error': str(e)}

# Example usage:
# result = predict_email_spam("Your email text here")
# print(result)
