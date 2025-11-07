import re
with open('job_apllications_emails.txt', 'r') as f:
    job_applications_emails = f.read()

name_Pattern = r"Name:(.+)"
name_match = re.findall(name_Pattern,job_applications_emails)
print("name")
for name in name_match:
  print(name)

email_pattern = r"[\w\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z]+"
email_match = re.findall(email_pattern,job_applications_emails)
print("email")
for email in email_match:
  print(email)

if email:
  break