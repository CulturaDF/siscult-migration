# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String

from settings import DATABASE_NAMES


class EntesMixin(object):
    __table_args__ = {'schema': DATABASE_NAMES.get('entes')}


class ProfileMixin(object):
    __table_args__ = {'schema': DATABASE_NAMES.get('perfis')}


class AdminMixin(object):
    __table_args__ = {'schema': DATABASE_NAMES.get('admin')}


class UserMixin(object):
    __table_args__ = {'schema': DATABASE_NAMES.get('usuarios')}


class ClassificacaoArtisticaMixin(object):
    id = Column(Integer, primary_key=True)
    descricao = Column(String(50))
