# Email-Spam-Detection-in-Python
This project is a Machine Learning-based Email Spam Detection System that classifies emails as Spam or Not Spam. It uses basic NLP techniques for text preprocessing and a Naïve Bayes classifier for classification. A simple Streamlit web app is included for real-time message validation.

🔹 Features:
Loads and cleans the Email Spam dataset.
Uses CountVectorizer (Bag of Words with stopword removal) for feature extraction.
Trains a Multinomial Naïve Bayes model to classify spam emails.
Provides an interactive Streamlit UI for testing email messages.

🔹 Tech Stack:
Python
1.pandas – For loading and preprocessing the dataset (pd.read_csv, .drop_duplicates, .rename, etc.).
2.scikit-learn (sklearn)
a)train_test_split – To split dataset into training and testing sets.
b)CountVectorizer – To convert text messages into a numerical matrix (Bag of Words representation).
c)MultinomialNB – Naïve Bayes classifier for training the spam detection model.
3.streamlit – To create a simple interactive web app where the user can input a message and check if it’s spam or not.

🔹 NLP Usage
This project applies NLP at a basic level using Bag of Words with stopword removal to transform raw email text into numerical features for classification.

🚀 How to Run the Project
📦 Required Libraries
Make sure you have Python 3.x installed. Install the following libraries before running the project:
pandas
scikit-learn
streamlit

You can install them all at once using:
pip install pandas scikit-learn streamlit

▶️ Run the Project
Navigate to the project folder and run the following command:
streamlit run spam_detection.py(Name of your file)

This will start the Streamlit app, and you’ll see a local URL (like http://localhost:8501) in your terminal. Open it in your browser to use the Email Spam Detection App.
