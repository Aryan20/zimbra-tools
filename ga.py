import subprocess
import csv

user_emails_string = subprocess.check_output(["zmprov", "-l", "gaa"], universal_newlines=True)
user_emails_list = user_emails_string.strip().split("\n")
with open('output_columns.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Name"])
        for user_email in user_emails_list:
                name = subprocess.check_output(["zmprov", "ga", user_email, "|", "grep", "sn"], universal_newlines=True)
                name = name.split("\n")[1][4::]
                writer.writerow([user_email, name])
