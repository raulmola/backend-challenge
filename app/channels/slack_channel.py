from channels import abstract_channel

class slack_channel(abstract_channel.abstract_channel):
    def __init__(self):
        self._description ="Mocked Slack Channel"

    @property
    def description(self):
        return self._description
    
    async def send(self, message):
        print (message)
