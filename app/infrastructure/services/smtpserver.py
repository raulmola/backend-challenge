from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Debugging

class BotSMTPServer:
    def __init__(self, config):
        self._config = config

    def start(self):
        controller = Controller(Debugging(), hostname=self._config["hostname"], port=self._config["port"])
        controller.start()



