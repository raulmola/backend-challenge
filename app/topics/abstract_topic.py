from abc import ABC, abstractmethod

class abstract_topic(ABC):
    @abstractmethod
    async def send(self, message):
        pass

    def set_channel(self, channel):
        self.channel = channel