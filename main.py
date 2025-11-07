import re

with open('job_apllications_emails.txt', 'r') as f:
    job_applications_emails = f.read()

name_Pattern = r"Name:(.+)"
name_match = re.findall(name_Pattern, job_applications_emails)
for name in name_match:
  print(name)