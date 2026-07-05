import os
import base64

from config import (
    AADHAAR_FOLDER,
    COLLEGE_FOLDER,
    RESUME_FOLDER,
    PHOTO_FOLDER
)

def save_attachment(service, message_id):

    message = service.users().messages().get(
        userId="me",
        id=message_id
    ).execute()

    payload = message.get("payload", {})
    parts = payload.get("parts", [])

    saved_files = []

    for part in parts:

        filename = part.get("filename")

        if not filename:
            continue

        body = part.get("body", {})

        attachment_id = body.get("attachmentId")

        if not attachment_id:
            continue

        attachment = service.users().messages().attachments().get(
            userId="me",
            messageId=message_id,
            id=attachment_id
        ).execute()

        file_data = base64.urlsafe_b64decode(
            attachment["data"]
        )

        lower = filename.lower()

        if "aadhaar" in lower:
            folder = AADHAAR_FOLDER

        elif "college" in lower:
            folder = COLLEGE_FOLDER

        elif "resume" in lower:
            folder = RESUME_FOLDER

        elif lower.endswith(".jpg") or lower.endswith(".jpeg") or lower.endswith(".png"):
            folder = PHOTO_FOLDER

        else:
            folder = "uploads"

        os.makedirs(folder, exist_ok=True)

        filepath = os.path.join(folder, filename)

        with open(filepath, "wb") as f:
            f.write(file_data)

        saved_files.append(filepath)

    return saved_files