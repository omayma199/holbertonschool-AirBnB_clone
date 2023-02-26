# holbertonschool-AirBnB_clone

![reference image](/airBnb.png)

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

## 3. Storage
All the classes are handled by the Storage engine in the FileStorage Class.


