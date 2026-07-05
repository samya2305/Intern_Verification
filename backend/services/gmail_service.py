import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail Read Only Permission
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# backend folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")


def gmail_login():
    creds = None

    # Load existing token
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )

    # Login if token doesn't exist
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES
            )

            creds = flow.run_local_server(
                host="127.0.0.1",
                port=8080,
                open_browser=True
            )

        # Save token
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service


def get_reply_emails():

    service = gmail_login()

    results = service.users().messages().list(
        userId="me",
        q="is:unread has:attachment"
    ).execute()

    return results.get("messages", [])


# Attachment download
from services.attachment_service import save_attachment


def download_all_attachments():

    service = gmail_login()

    messages = get_unread_emails()

    downloaded_files = []

    for message in messages:

        files = save_attachment(
            service,
            message["id"]
        )

        downloaded_files.extend(files)

    return downloaded_files