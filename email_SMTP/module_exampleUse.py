<<<<<<< HEAD
import smtplib
"""
hosts:
yahoo - smtp.mail.yahoo.com
google - smtp.gmail.com
hotmail - smtp.live.com
"""
my_email = "joker32567@gmail.com"
password = "791yO67G"
with smtplib.SMTP("smtp.gmail.com") as connection:
    # call TLS
    connection.starttls()
    # login
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nazar.ivankevych@yahoo.com",
        msg="Subject: This is a simple mail for testing\n\nHello there!"
    )

=======
import smtplib
"""
hosts:
yahoo - smtp.mail.yahoo.com
google - smtp.gmail.com
hotmail - smtp.live.com
"""
my_email = "joker32567@gmail.com"
password = "791yO67G"
with smtplib.SMTP("smtp.gmail.com") as connection:
    # call TLS
    connection.starttls()
    # login
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nazar.ivankevych@yahoo.com",
        msg="Subject: This is a simple mail for testing\n\nHello there!"
    )

>>>>>>> 6bb0f90e7b2042da98278b61b14da243c44df510
