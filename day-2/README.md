# MODULES & PACKAGES:
    What is a module?
    A module is a definitions file. It can contain function definitions,
    class definitions and variable assignments which we want to share across
    programs.

    It is a normal python file with .py extension, contains no executable
    statements.

    How to invoke a module?
    In whichever program, we need to use these definitions, we need to import
    that module
    >>> import modulename

    >>> import dsmodule

    What happens when we import a module?
    When we import a module for the first time, the module gets compiled and
    a .pyc file is generated and placed in folder called __pycache__

    For subsequent runs, Python will look into .pyc file and executes. This
    will hasten up the program execution and leaves the program in a perfect
    state.

    if we make changes in the source module file, .pyc is automatically
    reconstructed when imported again.

    from ... import clause:
    we can import specific items from a module using this syntax.Then there
    is no need to prefix the module name and .

    from dsmodule import f1,x
    f1()
    print (x)

    Aliasing:
    when two or more modules have same object name, this is very much handy
    to overcome the crisis.

    from dsmodule import f1 as ab
    from dsmodule1 import f1 as ac
    ab()
    ac()

    How to display the list of modules installed:
        >>> help ('modules')
    How to see the contents of a module:
        >>> import math
        >>> dir(math)
    How do you get information about any method of a module:
        >>> help(math.sqrt)

    How to install modules?
        by using a program called pip => python installer package. This
        program is available under scripts folder of python home folder

        a. must know the modulename correctly
        b. internet connection without firewalls
        c. should have privileges if required
        

# Interecting with Databases

1. SQL                  2. NoSQL

MySQL                       MongoDB
SQL Server                  Cassandra
Oracle                      Hbase



MySQL (back end):

    a. Database Server Installation
            a. username, password  (root, welcome@123)
    b. connect to database server 

Driver Installation: pymysql module  (installed)
                        c:\python39\scripts> pip install pymysql

                        c:\python39\scripts> pip show pymysql (to verify)

Python (3.0 or above):      python --version

connecting to the database server, needed parameters:
        a. ip address of the machine on which database server is running
        b. user name
        c. password
        d. database name
        e. port no (default)

how to connect?
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='training')


create a cursor object to perform sql commands:
y=x.cursor()
