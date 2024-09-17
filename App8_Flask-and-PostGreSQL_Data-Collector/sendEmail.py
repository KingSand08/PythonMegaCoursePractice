import smtplib, os
from email.mime.text import MIMEText
from dotenv import load_dotenv

def sendEmail(email, height, averageHeight, submissionCount):
        load_dotenv();
        fromEmail = os.getenv("EMAIL")
        fromPassword = os.getenv("PASSWORD")
        toEmail=email
        
        subject="Height Collector: Survey Response"
        message=f"Hey there, your height is <strong>{height} cm</strong>. Average height of all is <strong>{averageHeight} cm<strong/>, which is calculated out <strong>{submissionCount}</strong> of people."
        
        msg=MIMEText(message, 'html') # line will be read as html
        msg['Subject']=subject
        msg['From']=fromEmail
        msg['To']=toEmail
        
        gmail=smtplib.SMTP('smtp.gmail.com', 587) # Connects to Gmail's SMTP server on port 587, which is used for TLS encryption
        gmail.ehlo() #Sends an SMTP "EHLO" (Extended Hello) command to the server, which is part of the initial handshake
        gmail.starttls() # Upgrades the connection to a secure, encrypted SSL/TLS connection
        gmail.login(fromEmail, fromPassword) # Logs into your Gmail account using the App Password.
        gmail.send_message(msg) # Sends the email
        gmail.close() # Closes the connection to the SMTP server