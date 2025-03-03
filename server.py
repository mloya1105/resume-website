from flask import Flask, request, jsonify, render_template
import smtplib
import os
from dotenv import load_dotenv
from flask_cors import CORS  # Import the CORS module

load_dotenv()

# Fetch credentials from environment variables
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

app = Flask(__name__)

# Enable CORS for localhost (and production domain)
CORS(app, origins=["http://127.0.0.1:5000", "https://marissa-loya.com"])  # Allow localhost and production server

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/contact', methods=['POST'])
def contact():
    # Get form data
    data = request.form
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Log the incoming form data for debugging
    print(f"Received data: Name={name}, Email={email}, Message={message}")

    try:
        # Set up SMTP connection
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()  # Secure the connection
        smtp_server.login(EMAIL_USER, EMAIL_PASS)
        
        # Compose the email body
        email_body = f"Subject: Contact Form Submission\n\nFrom: {name} <{email}>\n\n{message}"
        
        # Send the email
        smtp_server.sendmail(email, EMAIL_USER, email_body)
        smtp_server.quit()

        # Log successful email sending
        print("Email sent successfully.")
        
        # Prepare response
        response = jsonify({"status": f"Thank you for your message, {name}! I'll be in touch soon."})
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000'  # Explicitly allow localhost
        
        # Return the success response
        return response, 200  # 200 OK status
    
    except smtplib.SMTPException as e:
        # Log specific SMTP exceptions
        print(f"SMTP error occurred: {str(e)}")
        response = jsonify({"status": "Error", "message": f"SMTP error: {str(e)}"})
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000'
        return response, 500

    except Exception as e:
        # Catch all other exceptions
        print(f"Unexpected error occurred: {str(e)}")
        response = jsonify({"status": "Error", "message": f"Unexpected error: {str(e)}"})
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000'
        return response, 500

if __name__ == "__main__":
    app.run(debug=True)  # Run the app with debug mode on for better logging
