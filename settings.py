# -*- coding: utf-8 -*-

# Definindo o modo debug para exibição de SQL construídos
# pelo SQLAlchemy
DEBUG = True

# URL de conexão com o MySQL para acessar os bancos
CONNECTION_URL = "mysql://root:root@localhost"

# Lista dos bancos de dados disponíveis para acesso
DATABASE_NAMES = {
    'entes': 'db_cgeac',
    'perfis': 'db_sccacult',
    'admin': 'db_sgucult',
    'usuarios': 'db_sgucult'
}
