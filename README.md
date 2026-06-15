# Spam-Email-Classifier-SEC-
# Spam Email Classifier using Machine Learning

## Project Overview

The Spam Email Classifier is a Machine Learning project developed to automatically classify messages as **Spam** or **Ham (Not Spam)**. The model is trained using Natural Language Processing (NLP) techniques and the SMS Spam Collection dataset. This project demonstrates the complete machine learning workflow, including data preprocessing, feature extraction, model training, evaluation, and prediction.

## Objectives

* Detect spam messages automatically.
* Apply NLP techniques for text classification.
* Train and evaluate a machine learning model.
* Save the trained model for future deployment and prediction.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* TF-IDF Vectorization
* Multinomial Naive Bayes
* Pickle

## Dataset

The project uses the SMS Spam Collection Dataset containing labeled SMS messages categorized as Spam or Ham.

## Methodology

### 1. Data Preprocessing

* Loaded and analyzed the dataset.
* Cleaned and prepared the text data.
* Converted categorical labels into numerical values.

### 2. Feature Extraction

* Applied TF-IDF (Term Frequency–Inverse Document Frequency) Vectorization.
* Transformed text messages into numerical feature vectors suitable for machine learning algorithms.

### 3. Model Training

* Split the dataset into training and testing sets.
* Trained a Multinomial Naive Bayes classifier on the processed data.

### 4. Model Evaluation

* Evaluated the model using test data.
* Generated classification metrics and confusion matrix.
* Achieved approximately 97% accuracy.

### 5. Prediction

* Tested the model with custom user messages.
* Successfully classified messages as Spam or Ham.

## Results

* High classification accuracy (~97%).
* Efficient spam detection using NLP techniques.
* Fast prediction performance with minimal computational requirements.

## Project Files

* Spam_Email_Classifier.ipynb – Complete project notebook.
* model.pkl – Trained machine learning model.
* vectorizer.pkl – Saved TF-IDF vectorizer.
* README.md – Project documentation.

## Learning Outcomes

Through this project, I gained practical experience in:

* Data preprocessing and cleaning.
* Natural Language Processing (NLP).
* Text feature extraction using TF-IDF.
* Machine Learning model training and evaluation.
* Model serialization using Pickle.
* Building end-to-end AI/ML workflows.

## Future Enhancements

* Deploy the model using Flask.
* Develop a web-based spam detection application.
* Experiment with advanced algorithms such as Logistic Regression and Support Vector Machines.
* Improve accuracy using hyperparameter tuning and feature engineering.

## Author

Sai Pranathi

Third Year Undergraduate Student

AI & Machine Learning Internship Project
