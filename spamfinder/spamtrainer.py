import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

spam_df = pd.read_csv('spam.csv')

spam_df['spam'] = spam_df['Category'].apply(lambda row: 1 if row == 'spam' else 0)

x_train, x_test, y_train, y_test = train_test_split(spam_df.Message, spam_df.spam)

cv = CountVectorizer()
x_train_count = cv.fit_transform(x_train.values)

model = MultinomialNB()
model.fit(x_train_count, y_train)

email_ham = ["Hey can you send me the current schedule?"]
email_ham_count = cv.transform(email_ham)
res = model.predict(email_ham_count)


x_test_count = cv.transform(x_test)
res_x_test = model.predict(x_test_count)
score_x_test = model.score(x_test_count, y_test)

joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(cv, 'count_vectorizer.pkl')