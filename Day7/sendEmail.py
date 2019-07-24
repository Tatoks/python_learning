import smtplib
try:
    s = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    s.starttls()
    s.login("sanne_abhi@yahoo.com", "yahoopassw0rd")
    message = "This message is from python"
    s.sendmail("sanne_abhi@yahoo.com", "sanne_abhi@yahoo.com", message)
    s.quit()

except Exception as e:
    print(e)