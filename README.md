# holbertonschool-AirBnB_clone

![reference image](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/1200px-Airbnb_Logo_B%C3%A9lo.svg.png)

##  1.Introduction
The console is a command interpreter to manage objects abstraction between objects and how they are stored.


The console will perform the following tasks:

- create a new object
- retrive an object from a file

- do operations on objects
- destroy an object

##  2.Available Command:
The commands available for this command interpreter are:



| Name     | Description  | command usage    |
| ------------- | ------------- |---------------|
|  *create       | Creates a new instance of the class passed by argument.| create <class_name>|
|   show      | Prints the string representation of an instance.  | show <class_name> <object_id> ; <class_name>.show(<object_id>)()       
|  *destroy       | Deletes an instance that was already created.         | destroy <class_name> <object_id ; <class_name>.destroy(<object_id>)()
|   all     | Prints string representation of all instances or of all instances of a specified class.        |all <class_name> ; <class_name>.all()
|  *update       | Updates an instance attribute if exists otherwise create it.         |update <class_name> <object_id> <attribute name> “<attribute value>” ; <class name>.update(<object_id>, <attribute name>, <attribute value>) ; <class name>.update(<object_id>, <dictionary representation>)
|   help      | Show all commands or display information about a specific command.         | help ; help <command_na
|   quit     | Exit the console.         |quit
|   EOF      | Exit the console.         |EOF ; (ctrl + d)

To start console type in shell

    AirBnB_clone$ ./console.py 
    (hbnb) 


### Create
To create an object use format "create" ex:

    (hbnb) create BaseModel

Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

    $./console.py
    (hbnb) create BaseModel
    119be863-6fe5-437e-a180-b9892e8746b8
    (hbnb) quit
    $ cat file.json ; echo ""
    {"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8":{"updated_at": "2019-02-17T2
    1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "_class_": "Base
    Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}

### Show
    
    (hbnb) show BaseModel 123-123-123.
Prints the string representation of a class instance based on a given id.

    $ ./console.py
    (hbnb) create User
    1e32232d-5a63-4d92-8092-ac3240b29f46
    (hbnb)
    (hbnb) show User    1e32232d-5a63-4d92-8092-ac3240b29f46
    [User]  (1e32232d-5a63-4d92-8092-ac3240b29f46)  {'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.  datetime(2019, 2, 17, 21, 34, 3, 635828), 
    'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
    (hbnb) 
    (hbnb) User.show    (1e32232d-5a63-4d92-8092-ac3240b29f46)
    [User]  (1e32232d-5a63-4d92-8092-ac3240b29f46){'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.   datetime(2019, 2, 17, 21, 34, 3, 635828), 
    'updated_at': datetime.datetime(2019, 2,    17, 21, 34, 3, 635828)}
    (hbnb) 

### Destroy
To Delete an instance of an object use "destroy id". ex:

    (hbnb) destroy BaseMOdel 123-123-123.
Deletes a class instance based on a given id. The storage file file.json is updated accordingly.

    $ ./console.py
    (hbnb) create State
    d2d789cd-7427-4920-aaae-88cbcf8bffe2
    (hbnb) create Place
    3e-8329-4f47-9947-dca80c03d3ed
    (hbnb)
    (hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
    (hbnb) Place.destroy(03486a3e-8329-4f47-9947-dca80c03d3ed)
    (hbnb) quit
    $ cat file.json ; echo ""
    {}

### all  or all BaseModel or BaseModel.all()

Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.

    $ ./console.py
    (hbnb) create BaseModel
    fce2124c-8537-489b-956e-22da455cbee8
    (hbnb) create BaseModel
    450490fd-344e-47cf-8342-126244c2ba99
    (hbnb) create User
    b742dbc3-f4bf-425e-b1d4-165f52c6ff81
    (hbnb) create User
    8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
    (hbnb)
    (hbnb) all BaseModel
    ["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99){'updated_at': datetime.da
    tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
    , 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
    eModel] (fce2124c-8537-489b-956e-22da455cbee8){'updated_at': datetime.datetime
    (2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
    21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
    (hbnb)
    (hbnb) User.all()
    ["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe){'updated_at': datetime.datetim
    e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
    , 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] 
    (b742dbc3-f4bf-425e-b1d4-165f52c6ff81){'updated_at': datetime.datetime(2019, 2
    , 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
    15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
    (hbnb) 
    (hbnb) all
    ["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe){'updated_at': datetime.datetim
    e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
    , 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
    del] (450490fd-344e-47cf-8342-126244c2ba99){'updated_at': datetime.datetime(20
    19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
    45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
    c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
    1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
    4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
    537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
    3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
    ), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
    (hbnb) 

### Update

Update an instance based on the class name and id:

    (hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"

Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.

    $ ./console.py
    (hbnb) create User
    6f348019-0499-420f-8eec-ef0fdc863c02
    (hbnb)
    (hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
    (hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02){'created_at': datetime.datetime(
    2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
    time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
    ef0fdc863c02'}
    (hbnb)
    (hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, address, "98 Mission S
    t")
    (hbnb) User.show(6f348019-0499-420f-8eec-ef0fdc863c02)
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02){'created_at': datetime.datetime(
    2019, 2, 17, 21, 54, 39, 234382), 'address': '98 Mission St', 'first_name': 'Ho
    lberton', 'updated_at': datetime.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id
    ': '6f348019-0499-420f-8eec-ef0fdc863c02'}
    (hbnb)
    (hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02,{'email': 'holberton@h
    olberton.com', 'last_name': 'School'})
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02){'email': 'holberton@holberton.co
    m', 'first_name': 'Holberton', 'updated_at': datetime.datetime(2019, 2, 17, 21,
    54, 39, 234382), 'address': '98 Mission St', 'last_name': 'School', 'id': '6f34
    8019-0499-420f-8eec-ef0fdc863c02', 'created_at': datetime.datetime(2019, 2, 17,
    21, 54, 39, 234382)}
    (hbnb) 

### Quit 

  quit or EOF


## 3. Files 

| File Name    | Description and contents|
| ------------- | ------------- |
|   [console.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/console.py)   | This is the command interpreter file. 
|   [base_model.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)     | This file contains de class base_model and its methods like save(), str(), dict().       
|   [city.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/city.py)    | This file contains de class city.         
| [amenity.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/amenity.py)   | This file contains de class amenity.       
|  [place.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/place.py)     | This file contains de class place..      
|    [review.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/review.py)    | This file contains de class review.        
|     [state.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/state.py)     | This file contains de class state.        
|     [user.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/user.py)  | This file contains de class user.     
|    [file_storage.py](https://github.com/omayma199/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py)   | This file contains de class file_storage and its methods, like save(), reload(), all().       

## 4. Storage
All the classes are handled by the Storage engine in the FileStorage Class.

## 5. Execution
- in interacctive mode:

    $ ./console.py
    (hbnb) help

 Output:

    Documented commands (type help <topic>):
    ========================================
    EOF help quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $
    

## Authors
Mizouni Oumaima: https://github.com/omayma199

