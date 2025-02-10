recipient = input("Enter the recepient:")
message = input("Enter the message:")
name = input("Enter the name:")
subject = input("Enter the subject:")
version = float(input("Enter the version:"))
discount = float(input("Enter the discount:"))
status = int(input("Enter the status:"))
code = input("Enter the Code:")
location = input("Enter the location:")
age = int(input("Enter the age:"))
companyName = input("Enter the Company name:")
website = input("Enter the website:")
phone = input("Enter the phone:")
job_title = input("Enter the Job title:")
department = input("Enter the department:")

print(f"\nDear:{recipient}\n"
      f"{message}\n"
      f"From: {name}\n"
      f"Subject: {subject}\n"
      f"version:{version}\n")
print(f"Discount: {discount:.2f}\n")
print(chr(status))
print(f"Code:{code}\n",
      f"location:{location}\n"
      f"Age:{age}\n"
      f"Company Name:{companyName}\n"
      f"Website:{website}\n"
      f"Phone:{phone}\n"
      f"Job title{job_title}\n"
      f"Department:{department}")
