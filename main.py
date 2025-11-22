from flask import Flask
from google_sheet import get_new_rows, update_status
from outreach import process_lead

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ GBOB Auto System Running — by Liaqat"

if __name__ == "__main__":
    leads = get_new_rows()
    for lead in leads:
        process_lead(lead)
