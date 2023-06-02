from abc import ABC, abstractmethod

class abs_topic_strategies_repository(ABC):
    @abstractmethod
    async def get_topic_strategy(self, topic_name):
        pass

