# -*- coding: utf-8 -*-

from .connection import Connection, Session
from settings import CONNECTIONS, DEBUG

connection = Connection(origin=CONNECTIONS.get('origin'),
                        destination=CONNECTIONS.get('destination'),
                        echo=DEBUG)
