import os
import json
import smtplib
import pandas as pd
import streamlit as st
from groq import Groq
from email.mime.text import MIMEText

# read this from config
sender_details = {"sender_name": "Rakesh Nair", "sender_email": "puthugeorge@gmail.com"}

def create_personalised_email(name, email, sender):
    ''' This function will help to create personalised email using given name and email id using llama3'''

    os.environ["GROQ_API_KEY"]="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"
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
        st.write("Email Sent Successfully")
    except Exception as e:
        print("An error occurred: ", str(e))


def fetch_email_list_and_mail(name_list, email_list):
    ''' This function is used to get email id's from a list of the leads and send them customised email'''
    try:
        for name,email in list(zip(name_list,email_list)):
        # Display user name for whom personalised email is being sent
            st.write(f"Hi! {name}")
            email_content = create_personalised_email(name,email,sender_details)
            st.write("Personalised email content is ready for use")
            st.write(email_content)
            send_email('smtp.gmail.com',587, sender_details["sender_email"], 'emhjalypcrhehmgs', sender_details["sender_email"], email,'Enhance Your Data Journey with FOSFOR - A Game-Changer from LTIMindtree',email_content)
            st.write("**************************************************************************")
    except FileNotFoundError:
        print("File not found. Please check file path.")
    except Exception as e:
        print("An error occurred: ", str(e))
