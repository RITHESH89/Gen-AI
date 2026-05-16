import streamlit as st

st.title("Gen AI Application")

user_input = st.text_input("Enter your prompt")

if st.button("Generate"):
    if user_input:
        response = f"AI Response for: {user_input}"
        st.write(response)
    else:
        st.warning("Please enter a prompt")
