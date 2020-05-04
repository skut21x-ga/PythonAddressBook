from peewee import *

db = PostgresqlDatabase('Contacts', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    id = CharField()
    first_name = CharField()
    last_name = CharField()
    area_code = IntegerField()
    phone_number = IntegerField()



db.connect()

db.create_tables([Contact])