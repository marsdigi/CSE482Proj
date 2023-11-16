# app.py
import streamlit as st


import re
import nltk
import spacy
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob  # For sentiment analysis

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


#Cell for database connection and data loading
mongodb_uri = "mongodb+srv://CSE_Reddit_Scraper:GoGreen@datasciencebiolab.urjjj09.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
database_name = 'CSE_Reddit'
collection_name = 'CSE Better Data 1'

client = MongoClient(mongodb_uri)
db = client[database_name]
collection = db[collection_name]

df = pd.DataFrame(list(collection.find()))

client.close()  

# Cell for data preprocessing
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'\W', ' ', text)
    text = ' '.join([lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text) if word not in stop_words])
    return text

df['cleaned_body'] = df['body'].fillna('').apply(preprocess_text)

# Cell for keyword extraction and visualization
vectorizer = TfidfVectorizer(min_df=0.05, max_df=0.85, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['cleaned_body'])
feature_names = vectorizer.get_feature_names_out()

# Sum tfidf scores for each term across all documents
sums = tfidf_matrix.sum(axis=0)
data = [(term, sums[0, col]) for col, term in enumerate(feature_names)]
ranking = pd.DataFrame(data, columns=['term', 'rank']).sort_values('rank', ascending=False)

# Generate a word cloud for the top terms
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(ranking.head(100).values))
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()






















































































"""


def main():
    st.header("Project: Automated Event Detection and Summarization for Reddit")

    st.subheader("1. Problem Definition")
    
    st.text("1.1 Context and Challenge:")
    st.write("The surge in user-generated content on platforms like Reddit poses a challenge "
             "in manually identifying and summarizing significant events due to the sheer volume and unstructured nature of the data.")
    
    st.text("1.2 Objective:")
    st.write("Develop an automated system for event detection and summarization from Reddit data, "
             "focusing on generating concise, informative summaries of identified significant events or discussions.")

    st.subheader("2. Related Work")
    
    st.write("Studies in Natural Language Processing (NLP) have addressed similar problems, "
             "with methodologies involving event detection through topic modeling, clustering, and classification. "
             "Text summarization has explored both extractive and abstractive methods.")

    st.subheader("3. Proposed Solution")
    
    st.text("3.1 Overview:")
    st.write("The proposed solution leverages NLP and machine learning to methodically identify and summarize "
             "significant events from Reddit posts, extracting, processing, and analyzing textual data to create coherent summaries.")

    st.subheader("3.2 Methodology")

    st.subheader("3.2.1 Data Collection and Preprocessing")
    
    st.write("Utilize Reddit API and PRAW for data scraping.")
    st.write("Store relevant posts and comments in a MongoDB database.")
    st.write("NLP preprocessing steps include tokenization, lemmatization, and removal of stop words and non-relevant characters.")
    
    st.subheader("3.2.2 Event Detection")
    
    st.write("Keyword Extraction using TF-IDF.")
    st.write("Topic Modeling using LDA.")
    st.write("Classification/Clustering algorithms to group posts into distinguishable events or topics.")

    st.subheader("3.2.3 Text Summarization")
    
    st.write("Extractive Summarization: Identify and extract key sentences or phrases representing the essence of detected events.")
    st.write("Abstractive Summarization: Implement transformer-based models like GPT or BERT to generate concise and coherent summaries.")

    st.subheader("3.2.4 Evaluation")

    st.write("Implement ROUGE and BLEU metrics to assess the quality and relevance of generated summaries.")

    st.subheader("3.3 Technologies and Tools")

    st.write("Programming Language: Python")
    st.write("Libraries: PRAW, Spacy, scikit-learn, gensim, NLTK")
    st.write("Database: MongoDB")

    st.subheader("4. Expected Outcomes and Challenges")

    st.text("Outcomes:")
    st.write("The system is expected to autonomously detect and succinctly summarize significant events from Reddit data, "
             "providing users with quick, clear insights into ongoing global happenings.")

    st.text("Challenges:")
    st.write("Anticipated challenges include accurately identifying genuine events amidst noise, "
             "ensuring coherence and reflection of the event's essence, and handling the ambiguity of natural language.")

    st.subheader("5. Future Directions")

    st.write("Future enhancements may involve optimizing for real-time processing, "
             "expanding to multiple subreddits/platforms, and implementing a user interface for more accessible interaction.")

if __name__ == "__main__":
    main()
"""
