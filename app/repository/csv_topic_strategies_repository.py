import asyncio
import csv
import os
import logging
from filelock import FileLock
from repository.abs_topic_strategies_repository import abs_topic_strategies_repository

class csv_topic_strategies_repository(abs_topic_strategies_repository):
    def __init__(self):
        self.csvfilename = 'topic_strategies_repository.csv'
        self.csvfullfilepath = os.path.join(os.path.dirname(__file__), self.csvfilename)
        self.last_read = os.path.getmtime(self.csvfullfilepath)-1
        self.cache = {}

    async def get_topic_strategy(self, topic_name): 
        logging.info(f'Reading topic strategies from {self.csvfullfilepath}')
        self.cache_topic_strategies()
        return self.cache[topic_name]

    def cache_topic_strategies(self):
        last_modified = os.path.getmtime(self.csvfullfilepath)

        if last_modified > self.last_read:
            self.cache = {}
            lock = FileLock(f'{self.csvfullfilepath}.lock')
            with lock.acquire(timeout=1):
                with open(self.csvfullfilepath, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        self.cache [row[0]] = row[1]
            self.last_read = last_modified        

