import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def export_to_sheets(rows):
    creds = Credentials.from_service_account_file(
        os.getenv("GOOGLE_SHEETS_CREDENTIALS"),
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    service = build("sheets", "v4", credentials=creds)

    body = {
        "values": rows
    }

    service.spreadsheets().values().append(
        spreadsheetId=os.getenv("GOOGLE_SHEET_ID"),
        range="Sheet1!A1",
        valueInputOption="RAW",
        body=body
    ).execute()
