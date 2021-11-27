import string
import re
from nltk.stem import WordNetLemmatizer

import joblib
import pickle


def preprocessor(review):

    lemmatizer = WordNetLemmatizer()
    HTMLTAGS = re.compile('<.*?>')
    table = str.maketrans(dict.fromkeys(string.punctuation))
    remove_digits = str.maketrans('', '', string.digits)
    MULTIPLE_WHITESPACE = re.compile(r"\s+")

    review = HTMLTAGS.sub(r'', review)
    review = review.translate(table)
    review = review.translate(remove_digits)
    review = review.lower()
    review = MULTIPLE_WHITESPACE.sub(" ", review).strip()
    review = review.split()
    review = ' '.join([lemmatizer.lemmatize(word) for word in review])
    return review
               
def return_params(query, model):

    text = preprocessor(query)
    print(text)
    if model == '2class':
        load_model = joblib.load("svm_2class.sav")
        
    elif model == '3class':
        load_model = joblib.load("svm_3class.sav")
    
    res = load_model.predict([text])
    return (query, res[0])