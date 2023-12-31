# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Load the iris dataset
iris = sns.load_dataset('iris')

# Create a scatter plot using Plotly Express
fig = px.scatter(iris, x='sepal_width', y='sepal_length', color='species',
                 title='Sepal Width vs Sepal Length by Species')

# Save the iris dataset to a CSV file
iris.to_csv('iris_data.csv', index=False)

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('word_cloud_for_key_term__hamas_wordcloud.csv')

# Function to display different sections based on the selected tab
def display_section(selected_tab):
    if selected_tab == "Project Description":
        st.header("Project: Automated Event Detection and Summarization for Reddit")
        st.write("Developed by: Kevin Mok, Brendan Wieferich, Marshal DiGiovanni, Jacob House, Roshan Atluri")


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

    elif selected_tab == "Sentiment Scores":
        st.header("Sentiment Scores")
        st.write(df)  # Display DataFrame for the Sentiment Scores

    elif selected_tab == "Proposed Solution":
        st.header("Proposed Solution")
        st.write("Content for the Proposed Solution tab")

# Create sidebar with tabs
selected_tab = st.sidebar.radio("Navigation", ["Project Description", "Sentiment Scores", "Proposed Solution"])

# Display content based on selected tab
display_section(selected_tab)

if selected_tab == "Project Description":
    # Show the plot
    st.plotly_chart(fig)
