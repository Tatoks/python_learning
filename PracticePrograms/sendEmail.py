import smtplib

try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("user@gmail.com", "password")
    message = "This message is from python"
    s.sendmail("user@gmail.com", "user@yahoo.com", message)
    s.quit()

except Exception as e:
    print(e)
