import streamlit as st
from app_utils import *


# Streamlit App

# Initialize session state
if "email_ids" not in st.session_state:
    st.session_state.email_ids= ""

if "names" not in st.session_state:
    st.session_state.names = ""

if "submitted_data" not in st.session_state:
    st.session_state.submitted_data =[]

st.title("Welcome To Your AI Assistant SDR")

#use key arguments to reset text area
email_ids_key = "email_ids_key"
names_key = "names_key"

# Create a sidebar for input
st.sidebar.header("Please provide details of the leads")

# Input for names
st.sidebar.subheader("Enter names of the leads")
st.session_state.names = st.sidebar.text_area("Enter comma-separated name:", key = names_key, height=100, placeholder="John Doe, Jane Smith, Bob Johnson", value=st.session_state.names)

# Input for email IDs
st.sidebar.subheader("Enter email id of the leads")
st.session_state.email_ids = st.sidebar.text_area("Enter comma-separated email IDs:", key = email_ids_key, height=100, placeholder="john.doe@example.com, jane.smith@example.com, bob.johnson@example.com", value = st.session_state.email_ids)


# Submit button
submit_button = st.sidebar.button("Submit")

# Clear button
clear_button = st.sidebar.button("Clear")

# Function to process email IDs
def process_email_ids(email_ids):
    emaillist = [email.strip() for email in st.session_state.email_ids.split(",")]
    return emaillist

# Function to process names
def process_names(names):
    namelist = [name.strip() for name in st.session_state.names.split(",")]
    return namelist

# Main app content
if submit_button:
    try:
        # Process email IDs
        email_list = process_email_ids(st.session_state.email_ids)

        # Process names
        name_list = process_names(st.session_state.names)

        # Store input data in session state
        st.session_state.submitted_data = list(zip(name_list, email_list))

        fetch_email_list_and_mail(name_list, email_list)

    except Exception as e:
        st.error("An error occurred: " + str(e))

# Clear button
if clear_button:
    # Clear session state values
    st.session_state.email_ids = ""
    st.session_state.names = ""
    st.session_state.submitted_data = []
    email_ids_key ="email_ids_key" + "_"
    names_key = "names_key" +'_'
