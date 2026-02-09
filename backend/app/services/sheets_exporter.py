import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

load_dotenv()

def export_to_sheets(rows):
    # Read values from .env
    private_key = os.getenv("GOOGLE_PRIVATE_KEY")
    client_email = os.getenv("GOOGLE_CLIENT_EMAIL")
    project_id = os.getenv("GOOGLE_PROJECT_ID")
    sheet_id = os.getenv("GOOGLE_SHEET_ID")

    if not all([private_key, client_email, project_id, sheet_id]):
        raise Exception("Missing Google Sheets environment variables")

    # CRITICAL STEP: convert \\n → real new lines
    private_key = private_key.replace("\\n", "\n")

    # Create credentials info manually
    credentials_info = {
        "type": "service_account",
        "project_id": project_id,
        "private_key": private_key,
        "client_email": client_email,
        "token_uri": "https://oauth2.googleapis.com/token",
    }

    # Create credentials
    credentials = Credentials.from_service_account_info(
        credentials_info,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    # Build Sheets service
    service = build("sheets", "v4", credentials=credentials)

    # Append rows
    service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range="Sheet1!A1",   # ⚠️ change if your tab name is different
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": rows},
    ).execute()
