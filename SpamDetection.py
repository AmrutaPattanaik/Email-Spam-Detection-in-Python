import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st


data = pd.read_csv(r"D:\PROJECTS\Email spam detection\spam.csv", encoding="latin1")
data.drop_duplicates(inplace=True)

# Rename columns for clarity
data = data.rename(columns={'v1': 'Category', 'v2': 'Message'})

# Replace label values
data['Category'] = data['Category'].replace(['ham', 'spam'], ['Not Spam', 'Spam'])

mess = data['Message']
cat = data['Category']

mess_train, mess_test, cat_train, cat_test = train_test_split(mess, cat, test_size=0.2, random_state=42)
cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

# Creating Model
model = MultinomialNB()
model.fit(features, cat_train)

# Testing
features_test = cv.transform(mess_test)

# Predict Data
message = cv.transform(['Congratulations, you won a lottery']).toarray()
result = model.predict(message)
#print(result)
    
#creating Model
model = MultinomialNB()

model.fit(features, cat_train)

#Test our model

features_test = cv.transform(mess_test)

print(model.score(features_test, cat_test))

#predict Data

def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result
#put = predict('Congratulations, you won a lottery')
#print(output)
st.header ('Spam Detection')
output = predict('Congratulations, you won a lottery')

input_mess = st.text_input('Enter Message Here')
if st.button('Validate'):
    output = predict(input_mess)
    st.markdown(output)