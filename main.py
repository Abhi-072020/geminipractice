import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

headers = {
    'Content-Type': 'application/json',
}
input = str(input("Your question:>  "))

data = {
    "contents": [
        {
            "parts": [
                {"text": input}
            ]
        }
    ]
}
response = requests.post(url, headers=headers, params={'key': api_key}, json=data)
print(type(response))

if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    print(type(data))
    # Access the text value
    text_value = data["candidates"][0]["content"]["parts"][0]["text"]
    
    # Print the text value
    print(text_value)
else:
    print(f"Error: {response.status_code} - {response.text}")