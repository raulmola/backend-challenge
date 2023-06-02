import logging 
from topics import abstract_topic
from channels.slack_channel import slack_channel

class sales_topic(abstract_topic.abstract_topic):
    def __init__(self):
        self.channel = slack_channel()
        self

    async def send(self,message):
        logging.info(f'Sending notification to Sales via channel {self.channel.description}')
        await self.channel.send(message)