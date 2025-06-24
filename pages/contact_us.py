import streamlit as st


st.header("Contact me")
with st.form(key="email_form"):
    user_email=st.text_input("Enter your email")
    message=st.text_area("enter the message")
    button=st.form_submit_button("Submit")
    if button:
        print("pressed!")
