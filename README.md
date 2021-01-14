# Intro to Python

- What is Python?
  - Syntax
    - Whitespace (spaces not tabs). Python is a whitespace based language, this means it defines blocks of code using indentation, or whitespace, rather than by using brackets. Most languages are either bracket based or whitespace based, in order to define different blocks of code.
    - Modules: Python has a long list of [built-in modules](https://docs.python.org/3/library/), basically this is library code. yiu can create your own modules but will get to that later. To use a module:
    ``` import {modulename} ```
    You can also import functions from modules:
    ```from {modulename} import {function}```
  - Best practice
    - Python Enhancement Proposals (PEPs)
    - https://www.python.org/dev/peps/
    - [Code style](https://www.python.org/dev/peps/pep-0008/) 
  - Comments
    - Single line `#`
    - Multi-line `"""comment here"""` - not used
  
- Variables
  - Used for storing data  
  ```
  age = 28
  name, age, location = "Mike", 28, "Bath"
  ```
  - Must start with a letter or the underscore character 
  - Cannot start with a number
  - Alpha-numeric characters and underscores (A-z, 0-9, and _ )
  - Case-sensitive
  - Generally lowercase with underscores

- User Input
  - Used to get information from the user on the command line
  - use `\n` at the end to put user input on new line
  - Python will stop executing when it encounters an `input` call
  ```
  name = input("What is your name?\n")
  print("Your name is: " + name)
  ```

- Data Types
  - Simple: str, ing, float, bool (True, False)
  - Other:
    - [range](https://www.w3schools.com/python/ref_func_range.asp): a list of numbers starting from 0
    - Casting: `str()`,`int()`,`float()`
    - EXERCISE
  - Complex: `list`, `tuple`, `dict`, `set`
    - 4 data types that allow for storing multiple values (array), all can contain any data type
      - list: ordered, changeable, 0 indexed, allows dups 
        - ```names = ['mike', 'charlie', 'ash']```
      - Tuple: ordered, unchangeable, 0 indexed, allows dups
        - ```names = ('mike', 'charlie', 'ash')``` 
      - Set: unordered, unindexed, unchangeable, no dups, *can add new items*, can make immutable with `frozenset()`
        - ```names = {'mike', 'charlie', 'ash'}```
      - Dictionary: unordered, changeable, no dup keys
        - ```person =	{"name": "Mike", "age": 28, "location": "Bath"}``` 
        
- Working with array types
  - All 4 array types work basically the same, substituting the methods that cannot apply to each one. Lists & Dictionaries are most commonly used.
  - [list](https://www.w3schools.com/python/python_lists_methods.asp)
    - Access a single value: ``` names[0] ```
    - Access a value form the end: ``` names[-1] ```
    - Adding to end: ```names.append("sarah")```
    - Inserting at an index: ```names.insert(2, 'Felix')``` - inserts into index 2 and shunts values up
    - Append elements from one to another: ```names.extend(othernames)``` - can be a list, set, dict, tuple
    - Removing items: ```names.pop()``` - optional key argument. ```namess.remove("sarah") - remove first occurance of value
    - Slicing: ```names[2:5]``` - third fourth and fifth (first inclusive, second exclusive)
      - Slicing can be used to override values: ``` names[2:3] = ['John', 'Jess'] ``` will replace 3rd value with 2 values and shunt other values up
  - [dict](https://www.w3schools.com/python/python_dictionaries_methods.asp)
    - Works like a assoc array in PHP

### EXERCISE
``` 
TBC
```
#### ANSWER
```

```

- Operators
  - Math: ```+ - * / % ** (Exponential) // (floor division)```
    - There alot more Math functions in the [Math module](https://www.w3schools.com/python/module_math.asp) and some [built into Python core](https://www.w3schools.com/python/python_math.asp)
  - Assignment: ```= += -= *= /=```
  - Comparison: ```== != > < >= <=```
  - Logical: ```and, or, not - not(x < 5 and x < 10)```
  

- Conditionals
  - if
    - ``` if a == b: ```
  - elif
    - ``` elif a == c: ```
  - if ... else
    - ``` else: ```
  - Shorthand/ternary
    - ```if a > b: print("a is greater than b")```
    - ```print("A") if a > b else print("B")```
  
### EXERCISE
```
POSTS and POLES
```
#### ANSWER
```
import math

calcType = input('What kind of calculation do you want to do?'
                 '\n[1] Calculate the length of a fence'
                 '\n[2] Calculate how many posts and poles you will need\n')

print(calcType)

POST_LENGTH = 0.1
POLE_LENGTH = 1.5

if calcType == "1":
    posts = input('How many posts do you have?\n')
    poles = input('How many poles do you have?\n')

    if posts > poles:
        fenceLength = round((int(poles) * (POST_LENGTH + POLE_LENGTH)) + POST_LENGTH, 0)
    else:
        fenceLength = round(((int(posts)-1) * (POST_LENGTH + POLE_LENGTH)) + POST_LENGTH, 0)
    print('Your fence will be: ' + str(fenceLength) + 'm')

elif calcType == "2":
    fenceLength = float(input('How Long does your fence need to be?\n'))

    if fenceLength < (POST_LENGTH + POLE_LENGTH + POST_LENGTH):
        print("Fence must be over 1.6m")
    else:
        poles = math.ceil((fenceLength - POST_LENGTH) / POLE_LENGTH)
        posts = poles + 1
        print("You will need " + str(poles) + " poles and " + str(posts) + " posts")

else:
    print("Invalid option")
```

- Loops
  - while - loop until a condition is false
    - ``` while a < 5: ```
  - for - loop over a sequence: list, tuple, dict, set, string or range
    - ``` for name in names:```
    - ``` for letter in "Mike":```
  - break - stop a loop early
  - continue - skip current iteration
  - else: a one time completion block after `while` or `for` - not executed after a `break`
  
### EXERCISE:
```
Write a short program that prints each number from 1 to 100 on a new line. 
For each multiple of 3, print "Fizz" instead of the number. 
For each multiple of 5, print "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
```
#### ANSWER:
```
for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```
 
- Functions
  ```
  def do_thing(arg):
    print("doing a thing with " + arg)
    
  
  do_thing("stuff")
  ```
  - PEP-8: lowercase and _, 2 Line breaks after a function
  - `*args` - tuple of args for unknown amount
  - `**args` - dict of args for unknown args
  - `arg = 'value'` for default values
  - `return` to return values
  - Lambda/anonymous functions can be assigned to variables, with unlimited params and 1 expression
  ```
  sum = lambda a, b : a * b
  print(sum(4, 5)) # 20 
  ```

  - Scope
    - functional scope
    - global variables inherit from call
  - https://www.w3schools.com/python/python_variables_global.asp

- Modules
  - Import files into your code to achieve better separation
  ```
  import example # example.py
  from example import do_thing # do_thing function in example.py
  import services.example # services/example.py
  import services.example as example # alias to make using it easier
  ```
  - Generally architectures are applied by frameworks, for most scripts try to build all functions into a module, grouping similar functions the import those modules when needed

- Sorting
  - `sort()` method of a list will sort ascending or alphabetically
  - `sort(resever = True)` to sort descending
  - `reverse()` reverse the current order
  - `sort(key = function)` to sort by a function, will sort ASC or alphabetically depending whats returned
  - Example, sort by key:
  ```
  def sort_by_age(person):
    return person["age"]


  people = [{"name": "Mike", "age": 28}, {"name": "Sarah", "age": 12}, {"name": "John", "age": 45}]

  people.sort(key=sort_by_age)

  print(people)
  ```
  
- Package manager: PIP
  - A package manager is an online repository of libraries written by other developers for you to use. Most things you want to do that are non-trivial there will be a package that can do it for you, and can do it better than you can do it
  - Example, if you want to hash a password using [bcrypt](https://pypi.org/project/bcrypt/)
  - Pay attention to Python version, and check release history to see when last updated. DO NOT USE OUTDATED PACKAGES.
  ```
  pip install [package]
  pip list
  ```
  
- Working with files
  - You can work with text and binary files, we will just be working with text files
  - `file = open("example.txt")` will open a file resource
  - `open()` takes a optional second argument, "r", "a", "w" (deleted file contense) or "x" (create), "r" is default
  - `file.read()` will read the entire content of a file, or `file.read(5)` to specify char count
  - `file.readline()` to read the next line of a file
  - `file.close()` to close the resource
  - `file.write("content")` to write to a file opened using "w" or "a"
  - There is a built-in library for working with CSVs, the syntax is a bit long winded
  ```
  import csv

  data = []
  with open('data.csv') as file:
    csv_data = csv.DictReader(file)
    for row in csv_data:
        data.append(row)

  print(data) # will contain a list of dicts (ordered dicts but treat like a dict)
  ```
  - Writing to CSVs is pretty much the same
  ```
  import csv
  
  with open('data.csv', mode='w') as file:
    file_data = csv.writer(file, deliimiter=',', quotechar='"')
    file_data.writerow(['list', 'of', 'data', 'to', 'write'])
  ```
  - Generally using the CSV library is not recommended, pandas is much easier
  ```
  import pandas
  data = pandas.read_csv('data.csv')
  ```

- Working with MSSQL
  - Connect using pyodbc library
  - `pip install pyodbc`
  - Connecting varies between environments:
    - [Windows](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows)
    - [Mac](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX)
  - Once connected you use `conn.cursor()` to start a new query
  ```
  db = conn.cursor()
  db.execute('SELECT * FROM {dbname}.dbo.{tablename}')
  rows = db.fetchall() # gets all rows
  row = db.fetchone() # gets next row
  ```
  - Can be shorted to: `db.execute({query}).fetchall()`
  - can grab counts using: `db.execute({query}).rowcount`
  - Prepared statements only offer anonymous placeholders: `db.execute('SELECT * FROM {dbname}.dbo.{tablename} WHERE id = ?', id)`: the data is provided as additional arguments to execute in the correct order.
  - To run multiple queries with different data, use `db.executemany({query}, [(1), (2)])`: second argument should be a list of lists/tuples
    - This is not a transaction, individual queries can fail without affecting others. It is just a loop.

### EXERCISE
```
TBC
```
#### ANSWER
```
```

- OO Python
  - Python is an OO language so technically all data types are just built-in classes, like JavaScript. To make classes:
  ```
  class Sheep:
      def __init__(self, name, color):
          self.name = name
          self.color = color
          
          
      def eat(self, food):
          print(self.name + " is eating " + food)
          
          
  dolly = Sheep("Dolly", "green")
  dolly.eat("Grass") # Dolly is eating Grass
  ```

Homework:

### EXERCISE
``` 
Blackjack
```
#### ANSWER
```

```
