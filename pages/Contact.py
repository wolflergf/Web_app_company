import pandas as pd
import streamlit as st

from send_email import send_email

df = pd.read_csv("topics.csv")
st.header("Contact Me")
with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_topic = st.selectbox("What topic do you want to discuss?", df["topic"])
    raw_message = st.text_area("Your message")
    user_message = """\
Subject: New email from {}

From: {}
Topic: {}
{}
    """.format(
        user_email, user_email, user_topic, raw_message
    )
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_message)
        st.info("Your email was sent successfuly!")
