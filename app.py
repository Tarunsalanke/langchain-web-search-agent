from model import main as run_model
import streamlit as st

st.title("Wikipedia Web Search Assistant")
topic = st.text_input("Enter the topic you want to search about:")
if st.button("Search"):
    if topic:
        result = run_model(topic)
        st.write(result)
    else:
        st.write("Please enter a topic to search.")
