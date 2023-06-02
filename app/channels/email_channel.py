import os
from aiosmtplib import SMTP
from channels import abstract_channel

class email_channel(abstract_channel.abstract_channel):
    def __init__(self):
        self._subject = "Customer assistance required!"
        self._fromaddr = os.environ.get('MAILCHANNEL_FROM')
        self._toaddrs = os.environ.get('MAILCHANNEL_TO')
        self._hostname = os.environ.get('SMTPSERVER_HOSTNAME')
        self._port = os.environ.get('SMTPSERVER_PORT')
        self._description = f"Email Channel (sending as {self._fromaddr} to {self._toaddrs} at {self._hostname}:{self._port})"

    @property
    def description(self):
        return self._description

    async def send(self, message):
        msg =f'Subject: {self._subject}\n\n{message}'
        client = SMTP(hostname=self._hostname, port=self._port)
        await client.connect()
        await client.sendmail(self._fromaddr, self._toaddrs, msg)
        await client.quit()
