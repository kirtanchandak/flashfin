from flask import Flask, render_template, request, redirect, url_for
import requests,json
from dotenv import load_dotenv
import os
import ssl
import smtplib

load_dotenv()

url = os.getenv("FLASK_FIREBASE_URL")
response = requests.get(url)

if response.status_code == 200:  
    data = json.loads(response.text)
    emails = {}
    for unique_id in data:
        name = data[unique_id]['name']
        email = data[unique_id]['email']
        emails[name] = email
   
else:
    print(f'Error fetching data from {url}, status code: {response.status_code}')

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', emails=emails)

context = ssl.create_default_context()
mail_sender= os.getenv("FLASK_MAIL_SENDER")
mail_password= os.getenv("FLASK_MAIL_PASSWORD")

@app.route("/mail")
def mail():
    if request.method == 'POST':
       
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(mail_sender, mail_password)  
            smtp.sendmail(mail_sender, mail_reciever, em.as_string())  # type: ignore
            success=True
            redirect(url_for('mail'),success=success)
    else:
        success=False        
    return render_template('mail.html',email=email)
   