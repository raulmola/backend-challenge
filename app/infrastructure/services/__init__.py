
import logging
import os
from .smtpserver import BotSMTPServer

logging.info("Starting SMTP Server")
botSmtpServerConfig =  {'hostname': os.environ.get('SMTPSERVER_HOSTNAME'), 'port': os.environ.get('SMTPSERVER_PORT')}
botSmtpServer = BotSMTPServer(botSmtpServerConfig)
botSmtpServer.start()
