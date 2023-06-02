# script for sending message updates

import time
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


if __name__ == '__main__':
    send_sms()
