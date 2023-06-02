import logging
from channels.email_channel import email_channel
from channels.slack_channel import slack_channel
from topics.sales_topic import sales_topic
from topics.pricing_topic import pricing_topic
from repository.csv_topic_strategies_repository import csv_topic_strategies_repository

class topic_factory:

    repository = csv_topic_strategies_repository()
    
    topic_types = {
        "Sales": sales_topic,
        "Pricing": pricing_topic
     }
    channel_types = {
        "email_channel": email_channel,
        "slack_channel": slack_channel,
        }


    @staticmethod
    async def create(topic_name):
        try:  
            topic_class_name = topic_factory.topic_types[topic_name]
            topic_strategy_name = await  topic_factory.repository.get_topic_strategy(topic_name)
            channel_class_name = topic_factory.channel_types[topic_strategy_name]
            
            topicInstance = topic_class_name()
            channelInstance=  channel_class_name()

            topicInstance.set_channel(channelInstance)

            return topicInstance

        except KeyError as e:
            logging.exception("Invalid Topic: %s", topic_name)
            raise

