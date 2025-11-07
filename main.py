import re

with open('job_apllications_emails.txt', 'r') as f:
    job_apllications_emails = f.read()

x = re.findall("Name", job_apllications_emails)

print(x)