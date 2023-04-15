import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = "fathimasilviyak@gmail.com"
MY_PASSWORD = "create app password from google account"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="fathimasilviyak@gmail.com",
            msg = f"Subject: Monday Motivation\n\n{quote}"
    )
