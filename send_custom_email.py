import smtplib

#https://myaccount.google.com/lesssecureapps go here and turn on less secure apps

Email_Address = "your email address"
Password = "your email address password"

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Email_Address,Password)

    subject = "test email"

    body = "this is a test body message sent by python"

    msg = f'Subject: {subject} \n\n {body}'

    smtp.sendmail(Email_Address,"email address of a person that you want to send emails to",msg)

