import os

import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

# # Function to create word cloud with sentiment-based coloring using Plotly
# def create_wordcloud(sentiments, title="Word Cloud"):
#     fig = px.imshow(sentiments, color_continuous_scale="RdYlGn", title=title)
#     st.plotly_chart(fig)

# # Function to create a heatmap of sentiment scores using Plotly
# def create_heatmap(sentiments_df, title="Sentiment Heatmap"):
#     fig = px.imshow(sentiments_df, color_continuous_scale="RdYlGn_r", labels=dict(color="Sentiment Score"), title=title)
#     st.plotly_chart(fig)

# # Sample DataFrame for demonstration purposes
# descriptors_sentiments_data = {
#     'Positive': [0.5, 0.7, 0.3],
#     'Neutral': [0.2, 0.5, 0.1],
#     'Negative': [0.3, 0.2, 0.6]
# }

# descriptors_sentiments_df = pd.DataFrame(descriptors_sentiments_data, index=['Key Term 1', 'Key Term 2', 'Key Term 3'])

# # Display the word clouds and heatmap
# for key_term, column_data in descriptors_sentiments_df.iterrows():
#     # Create a DataFrame for the word cloud data for the current key term
#     wordcloud_df = pd.DataFrame(list(column_data.iteritems()), columns=['Term', 'Occurrences'])
    
#     # Create a word cloud for the current key term
#     create_wordcloud(wordcloud_df, title=f"Word Cloud for Key Term: {key_term}")

# # Create a heatmap of sentiment scores for all key terms
# create_heatmap(descriptors_sentiments_df, title="Sentiment Heatmap for Key Terms")

print("hello world")