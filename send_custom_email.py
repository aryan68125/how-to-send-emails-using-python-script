import smtplib

#https://myaccount.google.com/lesssecureapps go here and turn on less secure apps

Email_Address = "aryan68125@gmail.com"
Password = "Ilovetoneystark@3000"

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Email_Address,Password)

    subject = "test email"

    body = "this is a test body message sent by python"

    msg = f'Subject: {subject} \n\n {body}'

    smtp.sendmail(Email_Address,"aryan268859@gmail.com",msg)

