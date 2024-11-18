# AirBnB Clone Console - Morocco

This is a project to build a clone of [Airbnb](https://www.airbnb.com/) - the popular accommodation rental platform.
The project is divided into multiple phases, each one is built on top of the previous one.

The first phase is the console app that will allow us to interact with the Airbnb clone from the command line.
This is the first step towards building the AirBnB clone project.

## Table of Contents

* [1. Introduction](#1-Introduction)
* [2. Installation](#2-Installation)
* [3. Usage](#3-Usage)
* [4. Testing](#4-Testing)
* [5. Authors](#5-Authors)
* [6. License](#6-license)

## ``1-Introduction``

The Airbnb Clone Console is a command line tool that allows you to interact with the Airbnb Clone project.

## ``2-Installation``

1. Clone this GitHub repository to your local machine.

`git clone https://github.com/hagouchikarim/AirBnB_clone.git`

2.  Jump to the directory of the project.

`cd AirBnB-Clone` 

3.  Execute the console.py

`./console.py`

### Execution 

Interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non Interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## ``3-Usage``

* Start the console in the interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

* create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
(hbnb) create BaseModel
503d1313-743a-4c33-8927-b652d81e2d65
$
```

* show

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) show BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
[BaseModel] (503d1313-743a-4c33-8927-b652d81e2d65) {'id': '503d1313-743a-4c33-8927-b652d81e2d65', 'created_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496645), 'updated_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496650)}
(hbnb)
(hbhb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) all
[BaseModel] (503d1313-743a-4c33-8927-b652d81e2d65) {'id': '503d1313-743a-4c33-8927-b652d81e2d65', 'created_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496645), 'updated_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496650)}
(hbnb) all BaseModel
[BaseModel] (503d1313-743a-4c33-8927-b652d81e2d65) {'id': '503d1313-743a-4c33-8927-b652d81e2d65', 'created_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496645), 'updated_at': datetime.datetime(2024, 2, 10, 0, 38, 25, 496650)}
```
* destroy

>*Deletes an instance of a given class with a given ID.*
>*Update the file.json*

```bash
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 503d1313-743a-4c33-8927-b652d81e2d65
(hbnb) all
[]
```

* count 

> *Prints the number of instances of a given class.*

```bash
(hbnb) create User
ef8595de-6a2c-496a-af6d-d96f33b389f3
(hbnb) create User
feb9c2f0-6b4f-4dcd-b3ed-2faebc4ccbab
(hbnb) create User
edbc4a23-714a-4364-a52f-ac041042e4b0
(hbnb) User.count()
3
```

## ``4-Testing``

* unittest module
* File extension ``` .py ```
* Files and folders start with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run TEST interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run TEST non-interactive mode

To run the tests in non-interactive mode, and discover all the tests, you can use the command:

```bash
python3 -m unittest discover tests
```

## ``5-Authors``

-   [Karim ElHagouchi](https://github.com/hagouchikarim/)
-   [Yassine Ennaour](https://github.com/yas19sin/)

