import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "rsaa47942@gmail.com"
PASSWORD = "zpgc kqbx dker mkub"


now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index,data_row) in data.iterrows()}
print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs= birthday_person["email"], msg = contents)










