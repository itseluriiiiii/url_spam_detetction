# URL Spam Detection
A machine learning project that detects malicious URLs using a Random Forest Classifier trained on textual URL patterns. The model applies TF-IDF vectorization on character n-grams to identify suspicious or phishing links.

# Overview
This project implements a URL spam detection model that classifies URLs as benign or malicious using machine learning. It uses a dataset (malicious_phish.csv) of labeled URLs and trains a RandomForestClassifier to predict the type of unseen URLs.

# The model:
Cleans and normalizes URLs.
Transforms them using TF-IDF character n-grams.
Trains a Random Forest classifier.
Evaluates model performance with accuracy, confusion matrix, and classification report.

# Features
✅ Cleans and normalizes URLs (removes protocols, symbols, etc.)
✅ TF-IDF vectorization on character n-grams
✅ Random Forest classification for detection
✅ Model evaluation with confusion matrix and metrics
✅ Support for batch and single URL prediction

# Project Structure
```bash
url_spam_detection/
│
├── app.py                # Main script for training and testing
├── requirements.txt      # Python dependencies
```
# Installation
- Clone the repository:
```bash
git clone https://github.com/itseluriiiiii/url_spam_detetction.git
cd url_spam_detetction
```
- Install the required packages:
```bash
pip install -r requirements.txt
```
- Add your dataset:
Place your malicious_phish.csv file in the project directory by downloading it from Kaggle.

# Usage
- Run the project with:
  python app.py
  The script will:
  - Load and preprocess the dataset
  - Train a Random Forest model
  - Display model accuracy and confusion matrix
  - Predict and print results for sample URLs
  You can modify the test_urls list in app.py to test your own URLs.

# Example Output
```bash
Accuracy: 0.965
Classification Report:
              precision    recall  f1-score   support
benign           0.97      0.95      0.96      3000
malicious        0.96      0.97      0.97      3000
```

# URL Predictions:
- http://37.49.226.178/deusbins/deus.sh4 --> malicious
- https://www.youtube.com --> benign
- www.jscape.com/sshfactory/ --> benign
- https://linkedin.com --> benign

- The URL 'https://www.google.com' is predicted as: benign

# Dependencies

All dependencies are listed in requirements.txt
:
pandas
numpy
seaborn
matplotlib
scikit-learn
Install them via:
```bash
pip install -r requirements.txt
```


# Troubleshooting
- FileNotFoundError:
Ensure malicious_phish.csv is in the project directory.
- Matplotlib not displaying:
If you’re on a headless server, save the plot instead of showing it:
plt.savefig('confusion_matrix.png')
- Memory issues:
Try reducing dataset size (df.sample(n=10000)).
