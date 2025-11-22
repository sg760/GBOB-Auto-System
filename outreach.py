from gmail_sender import send_mail
from apollo import get_site_score
from google_sheet import update_status

def process_lead(row):
    email = row["Email"]
    name = row["Name"]
    website = row["Website"]

    score = get_site_score(website)

    message = f"""
Hi {name},

Thanks for your message!

📌 Automated Website Score: {score}/100  
📌 Your domain was analyzed by our GBOB Auto System.

If you need guest posting or content writing, I can help.

Regards,  
Liaqat  
GBOB Outreach Automation
"""

    send_mail(email, "Guest Post Details", message)
    update_status(email, "Replied")
