import smtplib

def send_mail():
    sever = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("mlindwa@gmail.com", "mojamojabilabila")
    subject = "Price down"
    body = "check out the amazon product link"
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
    "modi@gmail.com",
    "medi@telia.fi",
    msg
    )
    print('mail send ')
    server.quit()
# price of amazon product
if (price < 29999):
    send_mail()
