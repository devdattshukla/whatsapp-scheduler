import os
import requests

TOKEN = os.environ["TOKEN"]
PHONE_NUMBER_ID = os.environ["PHONE_NUMBER_ID"]

# 👉 YOUR WhatsApp number (test recipient)
TO_NUMBER = "919925210608"   # replace this

url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "messaging_product": "whatsapp",
    "to": TO_NUMBER,
    "type": "text",
    "text": {
        "body": "🎉 GitHub Actions test message successful!"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)
