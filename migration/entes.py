# -*- coding: utf-8 -*-

from migration import connection

ENTES_SQL = """
SELECT
	db_sgucult.fr_usuario.USR_NOME AS nome,
	db_cgeac.cge_enderecoente.tipoEndereco AS endereco,
	db_cgeac.cge_enderecoente.complemento AS complemento,
	db_cgeac.cge_enderecoente.logradouro AS logradouro,
	db_cgeac.cge_enderecoente.cep AS cep,
	db_cgeac.cge_enderecoente.bairro AS bairro,
	db_cgeac.cge_enderecoente.cidade AS cidade,
	db_cgeac.cge_enderecoente.uf AS uf
FROM db_sgucult.fr_usuario
INNER JOIN db_cgeac.cge_ente ON db_sgucult.fr_usuario.USR_CODIGO = db_cgeac.cge_ente.codUsuario
INNER JOIN db_cgeac.cge_enderecoente ON db_cgeac.cge_enderecoente.codEnte = db_cgeac.cge_ente.id;
"""

def fetch_entes():
    """
    Efetua a consulta dos entes ao banco
    e que usa de introspeccao para gerar os
    objetos do Ente.
    """
    return connection.origin.execute(ENTES_SQL).fetchall()
