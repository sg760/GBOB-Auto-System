import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet():
    creds_json = os.getenv("SERVICE_ACCOUNT_JSON")
    creds = json.loads(creds_json)

    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
    client = gspread.authorize(credentials)

    sheet_id = os.getenv("SHEET_ID")
    return client.open_by_key(sheet_id).sheet1

def get_new_rows():
    sheet = connect_sheet()
    rows = sheet.get_all_records()
    return [r for r in rows if r["Status"] == "Pending"]

def update_status(email, new_status):
    sheet = connect_sheet()
    data = sheet.get_all_records()

    for index, row in enumerate(data, start=2):
        if row["Email"] == email:
            sheet.update_cell(index, 5, new_status)
            break
