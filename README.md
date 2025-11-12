Title:
SMS Spam Detection using Machine Learning

Project Overview:
This project is a machine learning-based system that classifies SMS messages as either spam or ham (not spam). It uses the Multinomial Naive Bayes algorithm trained on a labeled dataset of real-world SMS messages. The model is deployed using Streamlit to provide a simple, interactive web interface for users to test messages in real time.

Objectives:
To preprocess and analyze SMS text data.
To train a machine learning model that accurately detects spam messages.
To build an interactive Streamlit web application for real-time prediction.

Technologies Used:
Python, Scikit-learn, Pandas, NumPy, Streamlit, Joblib

Model Details:
Algorithm used: Multinomial Naive Bayes
Vectorization: CountVectorizer or TF-IDF
Accuracy achieved: 97.5%
Precision: 96.2%
Recall: 98.1%
F1-score: 97.1%

How to Run the Project:
Clone or download the project folder from this repository.
(Optional) Install the required dependencies if you have a requirements.txt file.
Run the Streamlit app using the command:
streamlit run app.py
Enter a text message and check whether it is spam or ham.

Dataset:
The dataset used for training was collected from publicly available SMS Spam datasets such as those on Kaggle. Each record contains a text message labeled as ‘spam’ or ‘ham’.
Due to file size limitations, the dataset is not included in this repository.

Author:
Developed by: Muhammad Sahal Thayyil
BCA - Yeldo Mar Baselios College
Affiliated to Mahatma Gandhi University

Future Enhancements:
Add support for multiple languages.
Integrate the system with chat or email platforms.

Use deep learning models to improve accuracy.
