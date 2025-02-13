from flask import Flask, request, jsonify
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch credentials
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    try:
        # Set up SMTP connection
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(EMAIL_USER, EMAIL_PASS)
        
        # Compose email
        email_body = f"Subject: Contact Form Submission\n\nFrom: {name} <{email}>\n\n{message}"
        
        # Send email
        smtp_server.sendmail(EMAIL_USER, "your_email@gmail.com", email_body)
        smtp_server.quit()
        
        return jsonify({"status": "Message sent successfully!"})
    
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)