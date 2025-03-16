##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import os
import random

import pandas as pd
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
smtp_host = os.getenv("MAILTRAP_SMTP_HOST")
smtp_port = os.getenv("MAILTRAP_SMTP_PORT")
smtp_user = os.getenv("MAILTRAP_USER")
smtp_pwd = os.getenv("MAILTRAP_PWD")
signature = "Tiger"

def choose_an_email_template(birthday_name):
    template_folder = Path("./letter_templates/")
    template_files = [str(f) for f in template_folder.glob("*.txt")]
    today_template = random.choice(template_files)

    with open(file=today_template) as email_template:
        message_body = email_template.read()
        message_body = message_body.replace("[NAME]", birthday_name)
        message_body = message_body.replace("[Signature]", signature)
    return message_body

def send_mail(birthday_name):
    # ----SEND MAIL----
    body = choose_an_email_template(birthday_name=birthday_name)
    sender = "Private Person <sender@example.com>"
    receiver = f"{birthday_name} <capybara@example.com>"

    message = f"Subject: Happy Day!\nTo: {receiver}\nFrom: {sender}\n\n{body}"
    print(message)
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pwd)
            server.sendmail(from_addr=sender,
                            to_addrs=receiver,
                            msg=message)


    except Exception as e:
        print(f"Failed to send email: {e}")


today = datetime.now()
df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    print(row["month"] , row["day"], row["name"])
    send_mail(row["name"])

print("=done=")

