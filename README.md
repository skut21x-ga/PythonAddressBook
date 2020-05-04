### Python Address Book 
#
#### Author

[Scott Kutler](scott.kutler@gmail.com)
#

### Screenshot
![Screenshot](https://github.com/skut21x-ga/PythonAddressBook/blob/master/shot.png?raw=true)
#

#### Function:

This app serves as a Contact Book with users able to create new contacts and also search contact by first name.
#
#### Technology Stacks used:

Python, SQL, and PeeWee
#
#### Setup Instructions:

##### 1. Fork & Clone this repo

##### 2. On the command line, CD into the lib folder in the root directory for this repo

##### 3. Install peewee If it's not installed

pipenv install peewee psycopg2 autopep8

##### 4. Start your command line Virtual Environment:

type 'pipenv shell' into command line

##### 5. Open PSQL to create a DB

In a seperate terminal tab/window type 'psql'

##### 6. Create a Database in PSQL

type 'CREATE DATABASE contacts;'

##### 7. Connect to new contacts DB

type '\c contacts;'

##### 8. Back in the PIPENV SHELL, Run the Address Book program

type 'python3 main.py' into command line

##### 9. Type 'exit' anytime to quit
#

##### Resources

http://patorjk.com/software/taag/ Used for Ascii ART
