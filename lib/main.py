from peewee import *

db = PostgresqlDatabase('Contacts', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    area_code = IntegerField()
    phone_number = IntegerField()



db.connect()

db.create_tables([Contact])

scott = Contact(first_name='Scott', last_name='Kutler', area_code = 469, phone_number = 3870895)
scott.save()
noah = Contact(first_name='Noah', last_name='Clark', area_code = 202, phone_number = 5555555)
noah.save()
roger = Contact(first_name='Roger', last_name='Campbell', area_code = 202, phone_number = 5551234)
roger.save()