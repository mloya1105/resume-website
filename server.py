from flask import Flask, request, jsonify, render_template
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch credentials
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

app = Flask(__name__)

# Serve the HTML page at the root URL
@app.route('/')
def home():
    return render_template('index.html')  # Make sure your HTML file is named 'index.html'

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
        smtp_server.sendmail(email, EMAIL_USER, email_body)
        smtp_server.quit()
        
        return jsonify({"status": "Thank you for your message, " + name + "! I'll be in touch soon."}), 200
    
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
