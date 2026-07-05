import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

AADHAAR_FOLDER = os.path.join(UPLOAD_FOLDER, "aadhaar")
COLLEGE_FOLDER = os.path.join(UPLOAD_FOLDER, "college")
RESUME_FOLDER = os.path.join(UPLOAD_FOLDER, "resume")
PHOTO_FOLDER = os.path.join(UPLOAD_FOLDER, "photo")

DATABASE_FOLDER = os.path.join(BASE_DIR, "database")

OFFER_CSV = os.path.join(DATABASE_FOLDER, "offer_data.csv")
VERIFIED_EXCEL = os.path.join(DATABASE_FOLDER, "verified.xlsx")