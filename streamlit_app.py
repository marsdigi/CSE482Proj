# app.py

import streamlit as st

def main():
    st.title("CSE-482 Project Application")
    
    # Add some text to the app
    st.write("CSE-482 Project app!")

    # Add a simple input widget
    user_input = st.text_input("Enter a value:")
    
    # Display a message based on user input
    if user_input:
        st.write(f"The value, {user_input}!")

    # Add the project text
    st.text("""
    User

    Project: Automated Event Detection and Summarization for Reddit

    1. Problem Definition

    1.1 Context and Challenge:
    The surge in user-generated content on platforms like Reddit poses a challenge in manually identifying and summarizing significant events due to the sheer volume and unstructured nature of the data.

    1.2 Objective:
    Develop an automated system for event detection and summarization from Reddit data, focusing on generating concise, informative summaries of identified significant events or discussions.

    2. Related Work

    Studies in Natural Language Processing (NLP) have addressed similar problems, with methodologies involving event detection through topic modeling, clustering, and classification. Text summarization has explored both extractive and abstractive methods.

    3. Proposed Solution

    3.1 Overview:
    The proposed solution leverages NLP and machine learning to methodically identify and summarize significant events from Reddit posts, extracting, processing, and analyzing textual data to create coherent summaries.

    3.2 Methodology:

    3.2.1 Data Collection and Preprocessing:

    Utilize Reddit API and PRAW for data scraping.
    Store relevant posts and comments in a MongoDB database.
    NLP preprocessing steps include tokenization, lemmatization, and removal of stop words and non-relevant characters.
    3.2.2 Event Detection:

    Keyword Extraction using TF-IDF.
    Topic Modeling using LDA.
    Classification/Clustering algorithms to group posts into distinguishable events or topics.
    3.2.3 Text Summarization:

    Extractive Summarization: Identify and extract key sentences or phrases representing the essence of detected events.
    Abstractive Summarization: Implement transformer-based models like GPT or BERT to generate concise and coherent summaries.
    3.2.4 Evaluation:

    Implement ROUGE and BLEU metrics to assess the quality and relevance of generated summaries.
    3.3 Technologies and Tools:

    Programming Language: Python
    Libraries: PRAW, Spacy, scikit-learn, gensim, NLTK
    Database: MongoDB
    4. Expected Outcomes and Challenges

    Outcomes:
    The system is expected to autonomously detect and succinctly summarize significant events from Reddit data, providing users with quick, clear insights into ongoing global happenings.

    Challenges:
    Anticipated challenges include accurately identifying genuine events amidst noise, ensuring coherence and reflection of the event's essence, and handling the ambiguity of natural language.

    5. Future Directions

    Future enhancements may involve optimizing for real-time processing, expanding to multiple subreddits/platforms, and implementing a user interface for more accessible interaction.
    """)

if __name__ == "__main__":
    main()
