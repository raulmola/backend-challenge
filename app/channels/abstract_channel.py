from abc import ABC, abstractmethod

class abstract_channel(ABC):
    @abstractmethod
    async def send(self, message):
        pass

    @abstractmethod
    def description(self, message):
        pass