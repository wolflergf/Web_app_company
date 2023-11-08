import streamlit as st

from send_email import send_email

st.header("Contact Me")
with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    user_message = """\
Subject: New email from {}

From: {}
{}
    """.format(
        user_email, user_email, raw_message
    )
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_message)
        st.info("Your email was sent successfuly!")
