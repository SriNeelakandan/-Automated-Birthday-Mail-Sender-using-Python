import datetime as dt
import pandas
import random
import smtplib

# ----------------------------- CONSTANTS ----------------------------- #
current_time = dt.datetime.now()
today_day = current_time.day
today_month = current_time.month
today_year = current_time.year

data = pandas.read_csv("birthdays.csv")
dictdata = data.to_dict(orient="records")

names = []
emails = []
created_letters = []

# ------------------------- SMTP MAIL SETUP --------------------------- #
my_mail = "YOUR_EMAIL_HERE"
my_password = "YOUR_PASSWORD_HERE"  # 🔐 Tip: Use environment variables instead

# --------- COLLECT NAMES & EMAILS OF TODAY'S BIRTHDAY PEOPLE -------- #
names = [x["name"] for x in dictdata if x["year"] == today_year and x["month"] == today_month and x["day"] == today_day]
emails = [x["email"] for x in dictdata if x["year"] == today_year and x["month"] == today_month and x["day"] == today_day]

# ------------------------- LOAD TEMPLATES ---------------------------- #
files = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt"
]

all_contents = [open(file, "r").read() for file in files]

if names:
    for name in names:
        random_letter = random.choice(all_contents)
        personalized = random_letter.replace("[NAME]", name)
        created_letters.append(personalized)

# --------------------------- SEND EMAIL ------------------------------ #
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=my_password)
    for i in range(len(names)):
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=emails[i],
            msg=f"Subject:Happy Birthday\n\n{created_letters[i]}"
        )
        print(f"Mail sent to {names[i]} successfully")

# ------------------- OPTIONAL: AUTOMATE THIS DAILY ------------------ #
# Tip: Deploy using www.pythonanywhere.com or a cron job.

# ---------------------------- NOTES ---------------------------------- #
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the file
# 3. If matched, pick a random letter, personalize it
# 4. Send the letter as an email
