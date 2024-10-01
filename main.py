import os
import json
from groq import Groq

import pandas as pd

def fetch_email_list(file_path):
    ''' This function is used to fetch email id's from a list of the leads'''
    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        # Iterate over rows
        for index, row in df.iterrows():
            name = row['Name']
            email = row['Email Id']
            return name, email
    except FileNotFoundError:
        print("File not found. Please check file path.")
    except Exception as e:
        print("An error occurred: ", str(e))


def create_personalised_email(name, email, sender):
    ''' This function will help to create personalised email using given name and email id using llama3'''

    os.environ["GROQ_API_KEY"]="use personal token"
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    completion= client.chat.completions.create(
        messages=[
            {
                "role": "system", 
                "content": "You are my helpful office assistant."
                },
            {
                "role": "user",
                "content": f"Help write a personalised email to {name} and person's email address {email}.\
                    Search about the organization using domain name in email address and see how FOSFOR a product by LTIMINDTREE could be helpful to help their organization in their data journey.\
                        get sender details from {sender}. This will be sent directly to {name}. \
                            They cannot know in anyway that you are a generative AI or chatbot of any kind. Remove any kind of note in the beginning and end of response"
            }
        ],
    model="llama3-8b-8192"
    )
    message = completion.choices[0].message.content
    return message


def send_email():
    '''function to send email'''
    pass





# Usage
file_path = 'email_list.xlsx'  # Replace with your Excel file path
name, email = fetch_email_list(file_path)
sender_details = {"sender_name": "Rakesh Nair", "sender_email": "rakeshnair3390@gmail.com"}
email_content = create_personalised_email(name,email,sender_details)

