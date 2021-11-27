import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def emailSendGrid(data):
    message = Mail(
        from_email='bbarryyim@gmail.com',
        to_emails='yimpact123@gmail.com',
        subject='New Visitor!',
        html_content='Visitor\'s IP: <strong>' + data['ipAddress'] + 
        '</strong><br> Time of Visit: <strong>' + data['firstVisit'] +
        '</strong><br> Browser: ' + data['browserInfo'])
    try:
        sg = SendGridAPIClient()
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)