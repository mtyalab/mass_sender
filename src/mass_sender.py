# script for sending message updates
import smtplib
import time
from email.message import EmailMessage
from time import sleep
from sinchsms import SinchSMS


# Function for sending SMS
def send_sms():
    # Enter all the details
    # get app_key and app_secret by registering
    # an app on sinchSMS
    number = 'your_mobile_number'
    app_key = 'your_app_key'
    app_secret = 'your_app_secret'

    # Enter tje message to be sent
    message = 'Hello there!!!'

    client = SinchSMS(app_key, app_secret)
    print("Sending '%s' to %s" % (message, number))

    response = client.send_message(number, message)
    message_id = response['messageId']
    response = client.check_status(message_id)

    # keep trying unless the status returned is Successful
    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)

    print(response['status'])


# Function for sending email notifications
def send_email(email: str):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = ""
    TO_EMAIL = email
    PASSWORD = ""

    msg = EmailMessage()
    msg['Subject'] = ''
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg.set_content('''
    ''', subtype='html')

    #     MESSAGE = f"""From: <{FROM_EMAIL}>
    # To: <{TO_EMAIL}>
    # Subject: Congratulations {first_name}
    #
    # Your merchant account has successfully been created.
    # To access your account, Go to https://merchant.com/login
    #
    # Regards,
    # Merchant Team
    # """

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    # smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.send_message(msg)
    smtp.quit()


if __name__ == '__main__':
    # send_sms() # un comment to enable sending with sms
    # send_email() # un comment to enable sending with email
    pass
