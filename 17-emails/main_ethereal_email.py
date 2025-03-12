# How Ethereal Works
## Send email by  ethereal.email
# it's only a fake SMTP service—it does not send real emails to external addresses like Gmail.
# It intercepts emails instead of delivering them.
# Emails sent using Ethereal stay in their dashboard for testing.
# You can check how your email looks without actually sending it to a recipient.
import smtplib

from_email = "alfred.block@ethereal.email"
password = "BRtBTeqaZ58gaVV3B2"
from_smtp = "smtp.ethereal.email"
to_email = "test@inbox.mailtrap.io"

with smtplib.SMTP(host=from_smtp, port=587) as connection:
    connection.starttls()
    print(connection)
    connection.login(user=from_email, password=password)
    connection.sendmail(
        from_addr=from_email,
        to_addrs=to_email,
        msg="Subject:Hello World!\n\nThis is the message from ethereal.email smtp for testing onlt! Thanks!"
    )