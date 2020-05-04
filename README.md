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

##### - You will need to create a new database called address_book and load the provided data in contacts from it. To do so:

##### Enter psql:

type 'psql' into command line

##### Create database:

type 'CREATE DATABASE address_book;' into command line

##### Connect to the address_book db to seed it:

type '\c address_book;' into command line

##### Then load the contacts.sql file to seed the db:

type '\i contacts.sql;' into command line

##### Start your command line Virtual Environment:

type 'pipenv shell' into command line

##### Run the python program

type 'python3 main.py' into command line

##### Type 'exit' anytime to quit
