import logging
from topics import abstract_topic
from channels.email_channel import email_channel

class pricing_topic(abstract_topic.abstract_topic):
    def __init__(self):
        self.channel = email_channel()

    async def send(self,message):
        logging.info(f'Sending notification to Pricing via channel {self.channel.description}')
        await self.channel.send(message)