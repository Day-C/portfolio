#!/usr/bin/python3
"""test filestorage."""
from models.base_model import Base_M


model = Base_M()
print(model)
model.save()
