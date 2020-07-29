import smtplib
from email.message import EmailMessage

email = input("Enter your email address > ")
emailpass = input("Enter the password for your email > ")


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = email
    msg['to'] = user
    password = emailpass

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

    if __name__ == '__main__':
        email_alert("Hey", "Hello World", "")
