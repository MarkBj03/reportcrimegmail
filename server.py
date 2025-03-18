from flask import Flask, request, redirect, url_for, render_template
import os
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Create the Flask server
server = Flask(__name__)

# Email configuration
EMAIL_ADDRESS = 'markbjnunez6@gmail.com'
EMAIL_PASSWORD = 'myub vnzr imyz gavv'  # Use the generated App Password here

# Route to handle form submission (Flask route)
@server.route('/submit', methods=['POST'])
def submit():
    try:
        # Retrieve form data
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phonenumber = request.form.get('phonenumber')
        crimetype = request.form.get('crimetype')
        description = request.form.get('message')  # Fix the field name
        uploaded_file = request.files.get('uploadedphoto')

        # Create email content
        email_subject = "New Crime Report"
        email_body = f"""
        --- Crime Report ---
        Submitted at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        First Name: {firstname}
        Last Name: {lastname}
        Email: {email}
        Phone Number: {phonenumber}
        Crime Type: {crimetype}
        Description: {description}
        Uploaded File: {uploaded_file.filename if uploaded_file else 'None'}
        ----------------------------
        """

        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        # Attach the uploaded file if it exists
        if uploaded_file and uploaded_file.filename:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(uploaded_file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {uploaded_file.filename}")
            msg.attach(part)

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        # Redirect to the thankyou.html page
        return redirect(url_for('thank_you'))

    except Exception as e:
        return f"An error occurred: {e}", 500

# Route to serve your custom thankyou.html (Flask route)
@server.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')  # This will render your custom thankyou.html

if __name__ == '__main__':
    server.run(debug=True)