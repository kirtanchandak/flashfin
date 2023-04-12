from flask import Flask, render_template
import requests,json

url = 'https://flashfin-4b7a6-default-rtdb.firebaseio.com/userData.json'
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
    for key, value in emails.items():
        return print(f" Hi {key}!! Your Email is  {value}", end="\n")
   