from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config.loadConfig import *
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def emailSendGrid(data):

    load_dotenv()
    config = loadConfigurations()

    message = Mail(
        from_email=config['sendGrid']['from_email'],
        to_emails=config['sendGrid']['to_emails'],
        subject='New Visitor!',
        html_content='Visitor\'s IP: <strong>' + data['ipAddress'] + 
        '</strong><br> Time of Visit: <strong>' + data['firstVisit'] +
        '</strong><br> Browser: ' + data['browserInfo'])
    try:
        sg = SendGridAPIClient(os.environ.get('sendGridApiKey'))
        response = sg.send(message)
        logging.info('Sending Email to: ' + str(config['sendGrid']['to_emails']) + ' || Status: '+str(response.status_code))
    except Exception as e:
        logging.error(e.message)