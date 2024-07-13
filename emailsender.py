############################################################################################
#python -m venv myenv
#pip install python-dotenv
    ###Make a .env file containing ur password and username##
'''
GMAIL_USER=xxxx@gmail.com
GMAIL_PASSWORD=pswd2121@
'''
#google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure"
#as a solution activate this feature from the following link:https://myaccount.google.com/lesssecureapps

############################################################################################

import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables from .env file
load_dotenv()
gmail_user = os.getenv('GMAIL_USER')
gmail_password = os.getenv('GMAIL_PASSWORD')

# Read emails from the text file
with open('emails.txt', 'r') as file:
    emails = [line.strip() for line in file.readlines()]

# Email content
subject = "The subject"
body = """\
Ur content
"""
attachment_path = 'C:/Users/marwane/Desktop/emails/xx.pdf'

# Setup the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)

for email in emails:
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    filename = os.path.basename(attachment_path)
    with open(attachment_path, "rb") as attachment:
        # Instance of MIMEBase and named as p
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

        # Encode into base64
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")

        # Attach the instance 'part' to instance 'msg'
        msg.attach(part)

    # Send the email
    text = msg.as_string()
    server.sendmail(gmail_user, email, text)
    print(f"Email sent to {email}")

server.quit()
