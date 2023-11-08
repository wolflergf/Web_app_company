import streamlit as st

st.header("Contact Me")
with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print(button)
        print("I was pressed!")
        print(user_email)
        print(user_message)
