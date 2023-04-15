import requests
import re
from pymongo import MongoClient
from dotenv import load_dotenv
import os

import smtplib

load_dotenv()

endpoint = "https://newsapi.org/v2/top-headlines"
params = {
    "apiKey": os.getenv("API_KEY"),
    'pageSize': 10,
    "country": "in",
    "category": "business"
}
def get_news():
    response = requests.get(endpoint, params=params)
    data = response.json()
    headlines = [article["title"] for article in data["articles"]]
    headline_string = "\n\n".join(headlines)
    return headline_string

url = os.getenv("DB_URL")
dbName = os.getenv("DB_NAME")

client = MongoClient(url)
db = client[dbName]
collection = db["userEmails"]
query = {"name": "inputs"}
projection = {"_id": 0,"inputs": 1}
results = collection.find_one(query,projection)
inputs_array = results["inputs"]
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv("MAIL")
smtp_password = os.getenv("MAIL_PWD")

subject = "News You Can Use: Our Latest News"
body_a = get_news()

body_a = re.sub(r'[^\x00-\x7F]+', '', body_a)

body = body_a

print(body)
print(f"Subject: {subject}\n\n{body}")
sender_email = smtp_username
recipients = inputs_array

def send_email():
    for recipient_email in recipients:
        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, message)
            print(f"Sent Mail succesfully to {recipient_email}")
send_email()            