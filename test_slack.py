import requests
import json

# Slack Webhook URL
slack_webhook_url = ''

# Message payload
message = {
    "text": "Hello, this is a message sent from my webhook!"
}

# Send the message
response = requests.post(slack_webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

# Check if the request was successful
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
