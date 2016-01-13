# -*- coding: utf-8 -*-

# Definindo o modo debug para exibição de SQL construídos
# pelo SQLAlchemy
DEBUG = True

# URL de conexão com o MySQL para acessar os bancos
CONNECTIONS = {
    'origin': 'mysql://root:root@localhost',
    'destination': 'postgresql+psycopg2://postgres:postgres@localhost/meta_id'
}

# Lista dos bancos de dados disponíveis para acesso
DATABASE_NAMES = {
    'entes': 'db_cgeac',
    'perfis': 'db_sccacult',
    'admin': 'db_sgucult',
    'usuarios': 'db_sgucult'
}
