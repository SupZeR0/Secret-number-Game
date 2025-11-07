from job_apllications_emails.txt import *
import re

name_Pattern = r"Name:(.+)"
name_match = re.findall(name_Pattern,job_applications_emails)
name