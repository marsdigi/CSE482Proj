# app.py

import streamlit as st
import pandas as pd

def main():
    st.title("Automated Event Detection and Summarization on Reddit")

    # Display a sample DataFrame
    st.subheader("Sample DataFrame:")
    sample_data = {'Column 1': [1, 2, 3, 4],
                   'Column 2': ['A', 'B', 'C', 'D']}
    df = pd.DataFrame(sample_data)
    st.dataframe(df)

    # User Input
    st.write("CSE-482 Project app!")

    # Add a simple input widget
    user_input = st.text_input("Enter a value:")
    
    # Display a message based on user input
    if user_input:
        st.write(f"The value, {user_input}!")

if __name__ == "__main__":
    main()
