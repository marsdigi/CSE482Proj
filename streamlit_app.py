# app.py

import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import pandas as pd

# Function to create word cloud with sentiment-based coloring
def create_wordcloud(sentiments, title="Word Cloud", colormap='RdYlGn'):
    # Generate a word cloud from the sentiments dictionary
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap=colormap).generate_from_frequencies(sentiments)

    # Display the word cloud
    st.pyplot(plt.figure(figsize=(10, 5)))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    st.pyplot()

# Function to create a heatmap of sentiment scores
def create_heatmap(sentiments_df, title="Sentiment Heatmap", cmap='RdYlGn_r'):  # Note: '_r' reverses the colormap
    st.pyplot(plt.figure(figsize=(10, 6)))
    sns.heatmap(sentiments_df, annot=True, cmap=cmap, fmt=".2f", linewidths=.5, cbar=False)
    plt.title(title)
    st.pyplot()

# Sample DataFrame for demonstration purposes
descriptors_sentiments_data = {
    'Positive': [0.5, 0.7, 0.3],
    'Neutral': [0.2, 0.5, 0.1],
    'Negative': [0.3, 0.2, 0.6]
}

descriptors_sentiments_df = pd.DataFrame(descriptors_sentiments_data, index=['Key Term 1', 'Key Term 2', 'Key Term 3'])

# Display the word clouds and heatmap
for key_term, column_data in descriptors_sentiments_df.iterrows():
    # Create a dictionary to store the word cloud data for the current key term
    wordcloud_dict = {}

    # Iterate over the rows of the DataFrame for the current key term
    for term, sentiment, occurrences in column_data.iteritems():
        # Add the term and its frequency (occurrences) to the dictionary
        wordcloud_dict[term] = occurrences

    # Create a word cloud for the current key term
    create_wordcloud(wordcloud_dict, title=f"Word Cloud for Key Term: {key_term}")

# Create a heatmap of sentiment scores for all key terms
create_heatmap(descriptors_sentiments_df, title="Sentiment Heatmap for Key Terms")
