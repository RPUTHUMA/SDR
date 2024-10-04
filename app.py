import streamlit as st
#from app_utils import * # to be used for groq
from app_utils_local import *


# Streamlit App

# Initialize session state
if "leads_data" not in st.session_state:
    st.session_state.leads_data= []

st.title("Welcome To Your AI Assistant SDR")

# Create a sidebar for input
st.sidebar.header("Please provide details of the leads")

# Input for names
st.sidebar.subheader("Enter details of the leads (separated by newline)")
lead_details = st.sidebar.text_area("Name, Email, Company, Linkedin Profile Url", height=200, placeholder="John Doe, johndoe@example.com, ABC Corp, https://www.linkedin.com/in/john-doe/\nJane Doe, janedoe@example.com, XYZ Inc, https://www.linkedin.com/in/jane-doe/")

# Submit button
submit_button = st.sidebar.button("Submit")

# Clear button
clear_button = st.sidebar.button("Clear")

# Main app content
if submit_button:
    try:
        # Split input into individual leads
        leads = lead_details.split("\n")
    
        # Initialize empty list to store lead data
        st.session_state.leads_data = []
        
        # Iterate over each lead
        for lead in leads:
            # Split lead data into name, email, company, linkedin
            lead_data = lead.split(",")
        
            # Validate lead data
            if len(lead_data) == 4:
                # Append lead data to session state
                st.session_state.leads_data.append({
                    "Name": lead_data[0],
                    "Email": lead_data[1],
                    "Company": lead_data[2],
                    "LinkedIn": lead_data[3]
                })
            else:
                st.error("Invalid lead data format. Please use: Name, Email, Company, LinkedIn URL")
        fetch_email_list_and_mail(st.session_state.leads_data)

    except Exception as e:
        st.error("An error occurred: " + str(e))

# Clear button
if clear_button:
    # Clear session state values
    st.session_state.leads_data = []