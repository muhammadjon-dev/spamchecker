import numpy as np
import joblib

# Load model and CountVectorizer
model = joblib.load('spam_classifier_model.pkl')
cv = joblib.load('count_vectorizer.pkl')

def checkspam(mail: str) -> bool:
    # Example email
    email_ham = [mail]

    # Vectorize email
    email_ham_count = cv.transform(email_ham)

    # Predict
    res = model.predict(email_ham_count)
    if res[0]:
        return True
    else:
        return False
    
print(checkspam("Hey can we meet today?"))
