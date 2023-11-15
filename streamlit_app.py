# app.py

import streamlit as st

def main():
    st.title("My Streamlit Application")
    
    # Add some text to the app
    st.write("Welcome to my Streamlit app!")

    # Add a simple input widget
    user_input = st.text_input("Enter your name:")
    
    # Display a message based on user input
    if user_input:
        st.write(f"Hello, {user_input}!")

if __name__ == "__main__":
    main()


