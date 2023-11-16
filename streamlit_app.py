# app.py

import streamlit as st

def main():
    st.title("CSE-482 Project Application")
    
    # Add some text to the app
    st.write("CSE-482 Project app!")

    # Add a simple input widget
    user_input = st.text_input("Enter your name:")
    
    # Display a message based on user input
    if user_input:
        st.write(f"Hello, {user_input}!")

if __name__ == "__main__":
    main()

