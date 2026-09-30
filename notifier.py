import os

import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("NTFY_URL")
topic = os.getenv("NTFY_TOPIC")


def send_notification(message):
    url = f"{base_url}/{topic}"
    requests.post(url, data=message)
