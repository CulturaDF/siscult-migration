# -*- coding: utf-8 -*-

from migration import connection

ENTES_SQL = """
SELECT
        db_cgeac.cge_ente.id AS ente_id,
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

CLASSIFICATIONS_SQL = """
SELECT DISTINCT
	area.descricao AS area,
	atuacao.descricao AS atuacao,
	estilo.descricao AS estilo
FROM
	db_cgeac.cge_areacultural area,
	db_cgeac.cge_atuacaoprof atuacao,
	db_cgeac.cge_estiloartistico estilo,
	db_cgeac.cge_ente_areacultural,
	db_cgeac.cge_ente
WHERE
area.id = db_cgeac.cge_ente_areacultural.idArea
AND atuacao.id = db_cgeac.cge_ente_areacultural.idAtuacao
AND estilo.id = db_cgeac.cge_ente_areacultural.idEstilo
AND cge_ente.id = db_cgeac.cge_ente_areacultural.idEnte AND cge_ente.id = {ente_id};
"""

def fetch_entes():
    """
    Efetua a consulta dos entes ao banco
    e que usa de introspeccao para gerar os
    objetos do Ente.
    """
    return connection.origin.execute(ENTES_SQL).fetchall()


def fetch_classification_ente(id):
    """
    Efetua a consulta das classificações artisticas
    do ente selecionado. A consulta sera feita pelo ID
    do mesmo.
    """
    return connection.origin.execute(
        CLASSIFICATIONS_SQL.format(ente_id=id)).fetchall()
