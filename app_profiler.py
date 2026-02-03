import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name ="Dr. Belle"
field = "Chemistry"
institution = "University of Stellenbosch"

# Display basic profile information
st.header("Researcher Overview")
st.write("**Name:** Dr. Belle")
st.write("**Field of Research:** Computational Chemistry")
st.write("**Institution:** University of Stellenbosch")

st.image(
    "https://github.com/DrBeeswax/css_streamlit_2026/blob/main/Profile%20Pic%20Email.jpg")

st.video("https://www.youtube.com/watch?v=CSUtadtfLh4")


# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data


# Add a contact section
st.header("Contact Information")
email = "belle@sun.ac.za"
st.write("You can reach Dr. Belle at belle@sun.ac.za.")