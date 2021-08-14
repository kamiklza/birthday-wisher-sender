##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



# ------------------------get month and day value-------------------------#
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day


# ------------------------read brithday.csv-------------------------#

import pandas
import random
import smtplib

email_list = pandas.read_csv("birthdays.csv")

for (index, row) in email_list.iterrows():
    if row.month == month and row.day == day:
        random_template = f"letter_{random.randint(1,3)}.txt"
        with open(f"letter_templates/{random_template}") as template:
            letter_template = template.read()
            new_letter = letter_template.replace("[NAME]", row.name_)


        my_email = "xxxxx"
        my_password = "xxxxxxx"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=row.email, msg=f"Subject: Happy Birthday {row.name_}!!! \n\n"
                                                                            f"{new_letter}")

# ------------------------Send email-------------------------#
