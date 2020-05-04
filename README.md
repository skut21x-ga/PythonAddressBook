### Address Book in Python / SQL

#### Author

[Scott Kutler](scott.kutler@gmail.com)

#### Function:

This app serves as a Contact Book with users able to create new contacts, see contacts in the address book, and also search contact by first or last name.

#### Technology Stacks used:

Python, SQL, and PeeWee

#### Setup Instructions:

##### - Fork & Clone this repo

##### - On the command line, CD into the lib folder in the root directory for this repo

##### Install peewee If it's not installed:

pipenv install peewee psycopg2 autopep8

##### Start your command line Virtual Environment:

type 'pipenv shell' into command line

##### Open PSQL to create a DB

In a seperate terminal window type 'psql'

##### Create a Database in PSQL:

type 'CREATE DATABASE contacts;'

#### Connect to Contacts DB:

type \c contacts

##### Back in the PIPENV SHELL, Run the Address Book program

type 'python3 main.py' into command line

##### Type 'exit' anytime to quit
