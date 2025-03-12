# Send and receive email using mailtrap
import random
import smtplib
import datetime
import unicodedata
from dotenv import load_dotenv
import  os
load_dotenv()
smtp_host = os.getenv("MAILTRAP_SMTP_HOST")
smtp_port = os.getenv("MAILTRAP_SMTP_PORT")
smtp_user = os.getenv("MAILTRAP_USER")
smtp_pwd = os.getenv("MAILTRAP_PWD")

# Use the datetime module to obtain the current day of the week
# Create a list of quotes from quotes.txt: list_quotes
# Pick a random quote from list_quotes
# Use smtplib to send an email receiver

def pick_a_quote():
    now = datetime.datetime.now()
    current_date_of_week = now.weekday()
    print(current_date_of_week)
    # if current_date_of_week == 0: # Only send email on Monday
    if True:
        with open("quotes.txt") as df:
            list_quotes = df.readlines()
            print(type(list_quotes))
            a_quote = random.choice(list_quotes)
            print(a_quote)
        a_quote = ((unicodedata.normalize("NFKD", a_quote)
                   .encode("ascii", "ignore"))
                   .decode("ascii"))
        return a_quote

#----SEND MAIL----
sender = "Private Person <test@email.com>"
receiver = "A Test User <test@email.com>"
body = pick_a_quote()
print(body)

message = f"""\
Subject: Dear Friend!
To: {receiver}
From: {sender}

{body}"""

print(message)

with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_pwd)
    server.sendmail(sender, receiver, message)

