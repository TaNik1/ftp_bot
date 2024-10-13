from .database import BaseModel
from peewee import IntegerField


class User(BaseModel):
    tg_id = IntegerField(default=0)
