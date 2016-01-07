# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from settings import CONNECTION_URL, DEBUG


def create_connection(connection_url=CONNECTION_URL, echo=DEBUG, **kwargs):
    """
    Define a conexão com o banco desejado, passando a URL de conexão.
    Também pode ser passado outros parametros como o ``echo`` e
    ``encoding``, por exemplo.
    """
    return create_engine(connection_url, echo=echo, **kwargs)
