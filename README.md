<img align="center" alt="hello world image" width="100%" height="300" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRir46C9dK0iBLo7wqsAnEVM20sj4KYwAvCiQ&usqp=CAU">

# AirBnB Clone Project
This is an Airbnb clone project that focuses on building a command-line interface (CLI) application, known as "The Console," to manage and interact with the backend data of the Airbnb clone. The application is written in Python and utilizes object-oriented programming concepts to provide a user-friendly interface for managing property listings, users, bookings, and more.

## Example of the Console
~/me$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
~/me$

## Purpose
The purpose of this project is to understand how to:
+ create a Python package
+ create a command interpreter using the cmd module
+ serialize and deserialize a Class
+ write and read a JSON file
+ manage datetime
+ handle named arguments in a function
+ How to use Args and Kwargs

## First step: Write a command interpreter to manage the AirBnB objects.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration�~@�

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place�~@�) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

## Resources used 
+ https://docs.python.org/3.8/library/cmd.html
+ http://pymotw.com/2/cmd/
+ https://docs.python.org/3.8/library/uuid.html
+ https://docs.python.org/3.8/library/datetime.html
+ https://docs.python.org/3.8/library/unittest.html#module-unittest
+ https://docs.python.org/3.8/library/unittest.html#module-unittest
+ https://www.pythonsheets.com/notes/python-tests.html
+ https://wiki.python.org/moin/CmdModule
+ https://realpython.com/python-testing/

## Concepts
+ https://intranet.alxswe.com/concepts/74
+ https://intranet.alxswe.com/concepts/66

## Requirements
+ Python Scripts
+ Allowed editors: vi, vim, emacs
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/usr/bin/python3
+ A README.md file, at the root of the folder of the project, is mandatory
+ Your code should use the pycodestyle
+ All your files must be executable
+ The length of your files will be tested using wc


## Author
© ___[Blessing Malik](https://github.com/chykB)___
