import json
import os

from dotenv import load_dotenv
from gphotospy import authorize


def initialize_gphoto_spy():
    """
    Creates the credentials file that gphotospy wants. Initializes the main
    service object with it.

    @return []
    """
    load_dotenv()
    PROJECT_ID = os.environ["PROJECT_ID"]
    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    credentials = {
        "web": {
            "project_id": PROJECT_ID,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        }
    }
    with open("credentials.json", "w") as f:
        json.dump(credentials, f)

    # Get authorization and return a service object
    service = authorize.init("credentials.json")
    return service
