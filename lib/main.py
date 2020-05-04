from peewee import *

db = PostgresqlDatabase('contacts', user='postgres',
                        password='', host='localhost', port='5432')


class BaseModel(Model):
    class Meta:
        database = db


class contacts(BaseModel):
    first_name = CharField()
    last_name = CharField()
    area_code = IntegerField()
    phone_number = IntegerField()


db.connect()
# db.drop_tables([contacts])
db.create_tables([contacts])

scott = contacts(first_name='Scott', last_name='Kutler',
                 area_code=469, phone_number=3870895)
scott.save()

noah = contacts(first_name='Noah', last_name='Clark',
                area_code=202, phone_number=5555555)
noah.save()

roger = contacts(first_name='Roger', last_name='Campbell',
                 area_code=202, phone_number=5551234)
roger.save()


def start():
    print('       Welcome to the Address Book!')
    print("   Type 'CREATE' to make a new contact,")
    print(" 'SEARCH' to search contacts by first name")
    print("             or 'EXIT' to quit")
    select = input()
    while select == 'CREATE':
        create()
    while select == 'SEARCH':
        search()
    while select == 'EXIT':
        exit()
    else:
        print(' Please type CREATE, SEARCH, or EXIT!')
        select = input()


def create():
    print('')
    print('------- ADD NEW CONTACT --------')
    print('')
    new_first = input('First Name: ')
    new_last = input('Last Name: ')
    new_areacode = input('Area Code): ')
    new_phonenumber = input('Phone Number (7 Digits): ')

    new_contact = contacts(
        first_name=new_first,
        last_name=new_last,
        area_code=new_areacode,
        phone_number=new_phonenumber
    )

    new_contact.save()
    print('')
    print('-------- CONTACT SAVED ---------')
    print('')
    start()


def search():
    contacts = contacts.select()
    for contact in contacts:
        print(contact.first_name)
    print('Please type full first name')
    search = input()
    if search == 'EXIT':
        start()
    elif search == 'contacts.first_name':
        contacts.get('Contact.first_name')
        print(
            f' Name: {contact.first_name} {contact.last_name} : {area_code}-{phone_number}')
        search()


start()
