from peewee import SqliteDatabase, Model

db = SqliteDatabase('project.db')


class BaseModel(Model):
    class Meta:
        database = db


def initialize_db():
    from .models import User
    db.connect()
    db.create_tables([User])
