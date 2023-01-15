import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD HERE"

now = dt.datetime.now()
today = (now.month, now.day)
current_year = now.year

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    name = (birthdays_dict[today]["name"])
    email = (birthdays_dict[today]["email"])

    random_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter}.txt") as data:
        letter = data.read()
        to_send = letter.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{to_send}"
        )


