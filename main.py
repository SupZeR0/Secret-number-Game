# from job_apllications_emails.txt import *
open(job_apllications_emails.txt)
import re

name_Pattern = r"Name:(.+)"
name_match = re.findall(name_Pattern,job_applications_emails)
for name in name_match:
  print(name)