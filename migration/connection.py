# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import CONNECTION_URL, DEBUG


class Connection(object):
    """
    Classe que define as conexões a serem usadas
    na migração. Ela possui duas engines:

        - origin: Conexão com o banco de origem, com os dados
        a serem migrados;
        - destination: Conexão com o banco de destino, que irá
        receber os dados na migração.
    """
    def __init__(self, *args, **kwargs):
        self._connection_origin = kwargs.pop('origin')
        self._connection_destination = kwargs.pop('destination')
        self._echo = kwargs.pop('echo', False)

        self.origin = self._create_connection_origin()
        self.destination = self._create_connection_destination()

    def _create_connection_origin(self):
        return create_engine(self._connection_origin, echo=self._echo)

    def _create_connection_destination(self):
        return create_engine(self._connection_destination,
                                           echo=self._echo)


class Session(object):
    """
    Classe que recebe as duas conexões, e oferece sessões
    para ambos os engines.
    """
    def __init__(self, *args, **kwargs):
        self._connection = kwargs.pop('bind')

        self._sessionmaker_origin()
        self._sessionmaker_destination()

    def _sessionmaker_origin(self):
        self.origin = sessionmaker(bind=self._connection.origin)

    def _sessionmaker_destination(self):
        self.destination = sessionmaker(bind=self._connection.destination)
