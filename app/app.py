from flask import Flask, render_template
import requests,json
from dotenv import load_dotenv
import os

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
   