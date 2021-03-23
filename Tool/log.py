# -*- conding:utf-8 -*-

import logging
from logging import config

class Log:

    def __init__(self):
        config.fileConfig("config.ini")
        self.log = logging.getLogger()