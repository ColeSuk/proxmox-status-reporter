import os

import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()


class ProxmoxConnector:
    def __init__(self):
        self.host = os.getenv("PROXMOX_HOST")
        self.token_id = os.getenv("PROXMOX_TOKEN_ID")
        self.token_secret = os.getenv("PROXMOX_TOKEN_SECRET")
        self.verify_ssl = os.getenv("PROXMOX_VERIFY_SSL", "False") == "True"

    def get(self, path):
        url = f"{self.host}/api2/json{path}"
        headers = {"Authorization": f"PVEAPIToken={self.token_id}={self.token_secret}"}
        response = requests.get(url, headers=headers, verify=self.verify_ssl)
        response.raise_for_status()
        return response.json()
