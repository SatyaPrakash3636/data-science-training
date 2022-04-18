# Core Python:

## Features:
    1. Portable
    2. Object oriented
    3. Compiled, Interpreted language
    4. Built on C API
    5. Interfacing with other languages & tools
    6. Scalability
    7. Dynamic programming
    8. Free and open
    9. Easy to use and debug

## Data types:
### Mutable & Immutable

- Immutable:
    - Numbers
    - Strings
    - Tuples

- Mutable:
    - Lists
    - Dictionaries

### Number:
- Any integer, float or complex value

### String:
- Anything enclosed in single or double quotes (readonly)

### Tuples:
- Static array (readonly array), created with `()`

### Lists:
- Dynamic array (can be changed), created with `[]`

### Dictionary:
- key, value pairs, hash tables, associative arrays, created with `{}`

## Variables:
A variable is the smallest program element to hold a value

variable=value

a. Should start with a **letter** or **_**
b. Case sensitive
c. No declaration, assignment will only create variables

    
    a=123                       # integer variable
    a=123.456                   # float variable
    a=2-3j                      # complex variable

    a='hp'                      # string variable
    a="Computer"                # string variable
    
    a=(1,'abc','pqr')           # tuple variable

    a=[1,2,3,'abc','pqr']       # list variable

    a={'p':1,'q':2,'r':3}       # dictionary variable


## I/O statements:
    input() => To accept values from the keyboard
    print() => To display values or messages

## String formatting:
    %                           String formatting operator
    .format()                   String formatting method
    f"Value of var is {var}"    Simplest way

## Popular IDLEs:
    1. Pycharm
    2. PyDev
    3. PyScripter
    4. Jupyter Notebook
    5. Komodo
    6. Standard IDLE

## General Functions:
- type(), print(), id(), del()

        >>> x=123
        >>> type(x)
        <class 'int'>
        >>> print (x)
        123
        >>> id(x)
        2212046330032
        >>> del(x)

## Number functions:
- int(), float(), complex()

## Strings, lists and tuples are known as sequences in Python

## String functions:
- str(), len(), max(), min(), + (concat)

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

- Multiline strings can be created by starting with 3 ''' or """ and ending with the same

## list functions:
- list(), len(), max(), min(), +
- Same indexing and sub-listing as that of strings

## tuple functions:
- tuple(), len(), max(), min(), +
- Same indexing and sub-tupling as that of strings


## dictionary functions:
- A collection of unordered pairs of keys and values. keys should be unique.
- len(), max(), min(), dict(), no +
        
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

## Comments:
    # comment            Single line comment
    ''' comments '''     Doc strings   

## Operators:
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

## Control Flow:
- if, for, while
        if cond:
            statement
        if cond:
            statements
        else:
            statement

        if cond:
            statements
        elif cond:
            statements
        elif cond:
            statements
        else:
            statement

        for variable(s) in sequence:
            statement

        while cond:
            statement

        while True:
            statements
            break


## Data object methods & sets:

### string functions:
        x='computer'
        (x is a string object, we can all methods of str class with x)

    upper(), lower(), title(), capitalize(), swapcase()
    count(), find(), replace(), startswith(), endswith()
    split(), join(), lstrip(), rstrip(), strip()
    encode(), decode(), isupper(), islower(), isdigit()
    isalpha(), isalnum(), isspace(), zfill(), center()
### list functions:
        append(), insert(), pop(), pop(n), remove()
        copy(), clear(), extend(), count(), index()
        reverse(), sort()
### dictionary functions:
        keys(), values(), items(), copy(), clear()
        pop(), update(), get(),
### tuple funtions:
        count(), index()
### number functions:
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
### set:    A colletion of unordered and unique values
    Set contains immutable data only - numbers, strings, tuples
### looping techniques:
        enumerate(), zip()
## User defined functions:

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

        c. User defined => user creates for his requirements

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

## Programs to be parts of User Defined Functions:
        1. creating and calling a function
        2. function with args and return value
        3. duck type programming
        4. functions as first class objects
        5. functions with keyword arguments
        6. global and local variables
        7. functions with variable length arguments
        8. map, filter and lambda
