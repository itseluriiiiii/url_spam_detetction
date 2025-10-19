
import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv('malicious_phish.csv')

df = pd.DataFrame(data)

# Reducing dataset
df = df.sample(n=10000, random_state=42)

print(df.head())

def clean_url(url):
    """Removes protocol and special characters from a URL."""
    url = re.sub(r'https?://(www\.)?', '', url)
    url = re.sub(r'[^\w\s]', '', url)
    return url.lower()

def train_model(df):
    """Trains a RandomForestClassifier on the given DataFrame."""
    df['clean_url'] = df['url'].apply(clean_url)

    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3))
    X = vectorizer.fit_transform(df['clean_url'])
    y = df['type']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    rf = RandomForestClassifier(
        n_estimators=50,
        max_depth=None,
        random_state=42
    )
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
                xticklabels=['benign', 'malicious'], yticklabels=['benign', 'malicious'])
    plt.title("Confusion Matrix - Random Forest")
    plt.show()

    return rf, vectorizer

# testing for multiple url's
def predict_urls(model, vectorizer, urls):

    clean_urls = [clean_url(url) for url in urls]
    vectors = vectorizer.transform(clean_urls)
    predictions = model.predict(vectors)

    print("\n🔍 URL Predictions:")
    for url, label in zip(urls, predictions):
        print(f"{url} --> {label}")

# testing for one url

def predict_single_url(model, vectorizer, url):

    clean_url_str = clean_url(url)
    vector = vectorizer.transform([clean_url_str])
    prediction = model.predict(vector)
    print(f"\nThe URL '{url}' is predicted as: {prediction[0]}")

if __name__ == "__main__":
    data = pd.read_csv('malicious_phish.csv')
    df = pd.DataFrame(data)
    df = df.sample(n=20000, random_state=42)

    print(df.head())

    # Train the model
    model, vectorizer = train_model(df)

    # Test with example
    test_urls = [
        "http://37.49.226.178/deusbins/deus.sh4",
        "https://www.youtube.com",
        "www.jscape.com/sshfactory/",
        "https://linkedin.com"
    ]
    predict_urls(model, vectorizer, test_urls)

    # Test a single URL
    predict_single_url(model, vectorizer, "https://www.google.com")
