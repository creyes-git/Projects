import smtplib
from email.message import EmailMessage
import ssl
import os

email_sender = os.getenv('email_sender')
email_password = os.getenv('email_password')

def send_email(body, title, email_receiver):
    """Send an email using Gmail's SMTP server.

       Parameters:
       body (str): The content of the email.
       title (str): The title of the email.
       email_receiver (str): The email of the receiver.

       Returns:
       None

       Raises:
       Exception: If there is an error when sending the email. """
       
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = title
    em.set_content(body)

    # Gmail SMTP Server Configuration (SSL/TLS)
    context = ssl.create_default_context()  # Create a secure SSL context

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:  # Use SMTP_SSL for secure connection
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")