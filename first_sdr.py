import os
import json
import smtplib
import pandas as pd
from groq import Groq
from email.mime.text import MIMEText

# read this from config
sender_details = {"sender_name": "Rakesh Nair", "sender_email": "puthugeorge@gmail.com"}

def create_personalised_email(name, email, sender):
    ''' This function will help to create personalised email using given name and email id using llama3'''

    os.environ["GROQ_API_KEY"]="Replace with groq key"
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


def send_email(smtp_server, smtp_port, username, password, from_addr, to_addr, subject, body):
    '''function to send email'''
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to_addr

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        print("Email Sent Successfully")
    except Exception as e:
        print("An error occurred: ", str(e))


def fetch_email_list_and_mail(file_path):
    ''' This function is used to fetch email id's from a list of the leads and send them customised email'''
    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        # Iterate over rows
        for index, row in df.iterrows():
            name = row['Name']
            email = row['Email Id']
            email_content = create_personalised_email(name,email,sender_details)
            send_email('smtp.gmail.com',587, sender_details["sender_email"], 'replace with app password', sender_details["sender_email"], email,'Enhance Your Data Journey with FOSFOR - A Game-Changer from LTIMindtree',email_content)
    except FileNotFoundError:
        print("File not found. Please check file path.")
    except Exception as e:
        print("An error occurred: ", str(e))


# Usage
file_path = 'email_list.xlsx'  # Replace with your Excel file path
fetch_email_list_and_mail(file_path)



