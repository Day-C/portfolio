#!/usr/bin/python3
""" test base models."""

from models.base_model import Base_M

bsm = Base_M()
print(bsm)

#test the to_dict method
bs = bsm.to_dict()
dsm = Base_M(**bs)
print(dsm)
