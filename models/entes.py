# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models import Base
from .mixins import EntesMixin, ClassificacaoArtisticaMixin


class AtuacaoCultural(EntesMixin, ClassificacaoArtisticaMixin, Base):
    """
    Modelo para mapeamento da tabela
    de areas culturais
    """
    __tablename__ = 'cge_atuacaoprof'

    def __repr__(self):
        return "<Atuacao Cultural(id={id}, descricao={descr})>".format(
            id=self.id,
            descr=self.descricao
        )


class AreaCultural(EntesMixin, ClassificacaoArtisticaMixin, Base):
    """
    Modelo para mapeamento da tabela
    de areas culturais
    """
    __tablename__ = 'cge_areacultural'

    def __repr__(self):
        return "<Area Cultural(id={id}, descricao={descr})>".format(
            id=self.id,
            descr=self.descricao
        )


class EstiloCultural(EntesMixin, ClassificacaoArtisticaMixin, Base):
    """
    Modelo para mapeamento da tabela
    de areas culturais
    """
    __tablename__ = 'cge_estiloartistico'

    idArea = Column(Integer, ForeignKey('area.id'))
    areas = relationship("AreaCultural", back_populates="estilos")

    def __repr__(self):
        return "<Estilo Cultural(id={id}, descricao={descr})>".format(
            id=self.id,
            descr=self.descricao
        )


AreaCultural.estilos = relationship(
    "EstiloCultural",
    order_by=EstiloCultural.id,
    back_populates="areas"
)
