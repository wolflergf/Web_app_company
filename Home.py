# Import necessary libraries
import pandas as pd
import streamlit as st

# Set Streamlit page configuration and title
st.set_page_config(layout="wide")
st.title("The Best Company")

# Create a multiline string for company description
about_company = """
Lorem ipsum dolor sit amet. Aut consequatur asperiores aut consequatur nesciunt aut fugit consequatur ea nobis unde.
Est mollitia dolores id itaque adipisci sed omnis cupiditate ut sint veritatis aut facere exercitationem et culpa corrupti.
Sit consequatur ipsum nam illo galisum aut officiis voluptatum sed ipsam internos aut similique consequatur sit porro eaque.
"""

# Display the company description
st.write(about_company)

# Define a header for the "Our Team" section
st.header("Our Team")

# Create a 3-column layout for team members
col1, col2, col3 = st.columns(3)

# Load team member data from a CSV file using pandas
df = pd.read_csv("data.csv", sep=",")

# Loop through and display the first 4 team members in the first column
with col1:
    for index, row in df[:4].iterrows():
        st.subheader("{} {}".format(row["first name"], row["last name"]).title())
        st.caption(row["role"])
        st.image("./images/" + row["image"])

# Loop through and display the next 4 team members in the second column
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader("{} {}".format(row["first name"], row["last name"]).title())
        st.caption(row["role"])
        st.image("./images/" + row["image"])

# Loop through and display the remaining team members in the third column
with col3:
    for index, row in df[8:].iterrows():
        st.subheader("{} {}".format(row["first name"], row["last name"]).title())
        st.caption(row["role"])
        st.image("./images/" + row["image"])
