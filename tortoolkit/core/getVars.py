# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]

# from ..core.database_handle import TorToolkitDB
from tortoolkit import SessionVars


def get_val(variable):
    return SessionVars.get_var(variable)
