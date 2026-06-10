import os
import json
import requests
from datetime import datetime

TOKEN = os.environ["TOKEN"]
PHONE_NUMBER_ID = os.environ["PHONE_NUMBER_ID"]

today = datetime.now().strftime("%m-%d")

print("Today:", today)

with open("contacts.json", "r") as f:
    contacts = json.load(f)

for contact in contacts:

    print("Checking:", contact["name"])
    print("Birthday:", contact["birthday"])

    # CHANGE TO True FOR TESTING
    if True:

        url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": contact["phone"],
            "type": "text",
            "text": {
                "body": f"🎂 Happy Birthday {contact['name']}! Wishing you a wonderful day and a happy year ahead."
            }
        }

        response = requests.post(url, headers=headers, json=data)

        print("STATUS CODE:", response.status_code)
        print("RESPONSE:", response.text)
