import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import pandas as pd

# Mocking up a sample DataFrame (Replace this with your actual data)
data = {
    'Term 1': {'Positive': 10, 'Neutral': 5, 'Negative': 2},
    'Term 2': {'Positive': 8, 'Neutral': 7, 'Negative': 3},
    'Term 3': {'Positive': 12, 'Neutral': 6, 'Negative': 1},
}

descriptors_sentiments_df = pd.DataFrame(data)

# Function to create word cloud with sentiment-based coloring
def create_wordcloud(sentiments, title="Word Cloud", colormap='RdYlGn'):
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap=colormap).generate_from_frequencies(sentiments)
    st.image(wordcloud.to_array(), caption=title, use_container_width=True)

# Function to create a heatmap of sentiment scores
def create_heatmap(sentiments_df, title="Sentiment Heatmap", cmap='RdYlGn_r'):
    plt.figure(figsize=(10, 6))
    sns.heatmap(sentiments_df, annot=True, cmap=cmap, fmt=".2f", linewidths=.5, cbar=False)
    st.pyplot()

def main():
    st.title("Sentiment Analysis App")

    # Display word clouds for each term
    for key_term, column_data in descriptors_sentiments_df.iterrows():
        wordcloud_dict = {term: occurrences for term, occurrences in column_data.items()}
        create_wordcloud(wordcloud_dict, title=f"Word Cloud for Key Term: {key_term}")

    # Display a heatmap of sentiment scores for all key terms
    create_heatmap(descriptors_sentiments_df, title="Sentiment Heatmap for Key Terms")

if __name__ == "__main__":
    main()


