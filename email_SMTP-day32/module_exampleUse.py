import smtplib
"""
hosts:
yahoo - smtp.mail.yahoo.com
google - smtp.gmail.com
hotmail - smtp.live.com
"""
my_email = "ivankevych32567@gmail.com"
password = "xP809RC6"
connection = smtplib.SMTP("smtp.gmail.com")
# call TLS
connection.starttls()
# login
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="nazar.ivankevych@yahoo.com", msg="Test out connections")

