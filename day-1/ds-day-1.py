Core Python:
Features:
    1. portable
    2. object oriented
    3. compiled, interpreted language
    4. built on C API
    5. Interfacing with other languages & tools
    6. scalability
    7. dynamic programming
    8. free and open
    9. easy to use and debug
Data types:
    mutable & immutable

    Immutable:
        numbers
        strings
        tuples

    Mutable:
        lists
        dictionaries

a)  number:
        any integer, float or complex value

b)  string:
        anything enclosed in single or double quotes (readonly)

c)  tuples:
        static array (readonly array), created with ()

d)  lists:
        dynamic array (can be changed), created with []

e)  dictionary:
        key, value pairs, hash tables, associative arrays, {}

Variables:
    A variable is the smallest program element to hold a value

    variable=value

    a. should start with a letter or _
    b. case sensitive
    c. no declaration, assignment will only create variables

    
    a=123                       # integer variable
    a=123.456                   # float variable
    a=2-3j                      # complex variable

    a='hp'                      # string variable
    a="Computer"                # string variable
    
    a=(1,'abc','pqr')           #tuple variable

    a=[1,2,3,'abc','pqr']       #list variable

    a={'p':1,'q':2,'r':3}       #dictionary variable


I/O statements:
    input() => to accept values from the keyboard
    print() => to display values or messages

String formatting:
    %           string formatting operator
    .format()   string formatting method


Popular IDLEs:
    1. Pycharm
    2. PyDev
    3. PyScripter
    4. Jupyter Notebook
    5. Komodo
    6. standard IDLE
    
HANDS ON:

General Functions:
            >>> x=123
            >>> type(x)
            <class 'int'>
            >>> print (x)
            123
            >>> id(x)
            2212046330032
            >>> del(x)

number functions:
            int(), float(), complex()
string functions:
            str(), len(), max(), min(), + (concat)
            >>> x='computer'
            >>> x[1]
            'o'
            >>> x[-1]
            'r'
            >>> x[2:]
            'mputer'
            >>> x[:7]
            'compute'
            >>> x[2:7]
            'mpute'
            >>> x[:]
            'computer'
            >>> x[-3:]
            'ter'
            >>> x[::-1]
            'retupmoc'
            >>> x[::-2]
            'rtpo'
            >>> x[::2]
            'cmue'
            >>>
            multiline strings can be created with 3 ''' or """ begin, end

list functions:
        list(), len(), max(), min(), +
        same indexing and sub-listing as that of strings
tuple functions:
        tuple(), len(), max(), min(), +
        same indexing and sub-tupling as that of strings

        strings, lists and tuples are known as sequences in Python
dictionary functions:
        A collection of unordered pairs of keys and values. keys are
        quoted, and unique. len(), max(), min(), dict(), no +
        
                >>> x={'a':123,'b':'abc','c':[1,2,3],'d':(4,5,6),'e':{'p':1,'q':2}}
                >>> len(x)
                5
                >>> max(x)
                'e'
                >>> min(x)
                'a'
                >>> a=dict()
                >>> a
                {}
                >>> x['c']
                [1, 2, 3]
                >>> x['c'][2]
                3
                >>>

comments:
            #        single line comment
            '''      at begin and end, to create multiline comments

Operators & Control Flow:
            Arithemetic:    +, -, *, /, %, **, //
            Relational:     >,>=,<,<=,==,!=
            Logical:        and, or, not
            Assignment:     +=,-=,*=,/=,**=,//=
            Membership:     in, not in
                                    variable in sequence
            Identity:       is , is not
                                    x is y (id(x) == id(y))
                                    x is not y (id(x) != id(y))
            Boolean:        True, False
            None:           x is None

            if, for, while => control flow

            if cond:
                statements

            if cond:
                statements
            else:
                statements

            if cond:
                statements
            elif cond:
                statements
            elif cond:
                statements
            else:
                statements


            for variable(s) in sequence:
                statements


            while cond:
                statements

            while True:
                statements
                break


3. data object methods & sets:
    string functions:
        x='computer'
        (x is a string object, we can all methods of str class with x)

    upper(), lower(), title(), capitalize(), swapcase()
    count(), find(), replace(), startswith(), endswith()
    split(), join(), lstrip(), rstrip(), strip()
    encode(), decode(), isupper(), islower(), isdigit()
    isalpha(), isalnum(), isspace(), zfill(), center()

    list functions:
        append(), insert(), pop(), pop(n), remove()
        copy(), clear(), extend(), count(), index()
        reverse(), sort()

    dictionary functions:
        keys(), values(), items(), copy(), clear()
        pop(), update(), get(),

    tuple funtions:
        count(), index()

    number functions:
        import math
        math.sqrt(144)

        'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
        'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh',
        'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1',
        'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
        'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite',
        'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma',
        'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter',
        'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin',
        'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp'

    set:    A colletion of unordered and unique values
            Set contains immutable data only - numbers, strings, tuples

    looping techniques:
        enumerate(), zip()


4. user defined functions:
    What is a function?
        A function is a sub program that can be called repetitively

    What is the anatomy of a function?
        a. declaration or prototype
        b. definition or body
        c. execution or call
    Python has definition and execution only

    What are the types of the functions?
        a. builtin => input(), print(), len(), max(), min(), list(), str()
        b. additional => part of various libraries (modules).
                         import math
                         math.sqrt(144)

                         import os
                         os.system ('cls')

        c. user defined => user creates for his requirements


        Ex:
            def fun1(args):
                statements
                return

            #definition
            def fun1():
                k=1
                while k<=3:
                    print ('Python')
                    k+=1
                return

            #call
            fun1()

            
        Programs to be parts of User Defined Functions:
            1. creating and calling a function
            2. function with args and return value
            3. duck type programming
            4. functions as first class objects
            5. functions with keyword arguments
            6. global and local variables
            7. functions with variable length arguments
            8. map, filter and lambda

            



        
        
        
                
                
                    

            






            

    


    




    
        
