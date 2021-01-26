# Intro to Python

- What is Python?
  - Syntax
    - Whitespace (spaces not tabs). Python is a whitespace based language, this means it defines blocks of code using indentation, or whitespace, rather than by using brackets. Most languages are either bracket based or whitespace based, in order to define different blocks of code.
    - Modules: Python has a long list of [built-in modules](https://docs.python.org/3/library/), basically this is library code. You can create your own modules but will get to that later. To use a module:
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
  - Simple: str, int, float, bool (True, False), None
  - Other:
    - [range](https://www.w3schools.com/python/ref_func_range.asp): a list of numbers starting from 0
    - Casting: `str()`,`int()`,`float()`
### EXERCISE
```
Write a script that asks the user for their name and age as 2 separate questions. 
Then print the following string with the correct data:
{name} will be {age} years old next year
```

#### ANSWER
```
name = input('What is your name?\n')
age = input('How old are you?\n')
print(name + ' will be ' + str(int(age)+1) + ' years old next year')
```

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
    - To find the index of a value: ``` names.index({value}) ```
    - Adding to end: ```names.append("sarah")```
    - Inserting at an index: ```names.insert(2, 'Felix')``` - inserts into index 2 and shunts values up
    - Append elements from one to another: ```names.extend(othernames)``` - can be a list, set, dict, tuple
    - Removing items:  
    ```names.pop()``` - optional key argument  
    ```names.remove("sarah")``` - remove first occurance of value  
    - Slicing
      - Slicing follows this rule: `list[start:stop:step]`
      - Omit any of the 3 to use their default: start = 0, stop: last element, step = 1
      - ```names[2:5]``` - third fourth and fifth (first inclusive, second exclusive)
      - Slicing can be used to override values: ``` names[2:3] = ['John', 'Jess'] ``` will replace 3rd value with 2 values and shunt other values up
  - [dict](https://www.w3schools.com/python/python_dictionaries_methods.asp)
    - Works like a assoc array in PHP

### EXERCISE
``` 
- 1. Output the first and last name of each person in this data, each person on a different line:
people = [{"firstname": "Mike", "lastname": "Oram"}, {"firstname": "Sarah", "lastname": "Jackson"}]

- 2. Add 7000 after 6000 is the following data:
data = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

- 3. Replace the first occurance of the number 20 with the number 200 from the below list:
data = [5, 10, 15, 20, 25, 50, 20]

- 4. Take the odd index items from list1 and the even index items from list2 and put them into a new list
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
```
#### ANSWER
```
1. 
print(people[0]["firstname"] + " " + people[0]["lastname"])
print(people[1]["firstname"] + " " + people[1]["lastname"])
# Mike Oram 
# Sarah Jackson

2.
data[2][2].append(7000)
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

3.
index = data.index(20)
data[index] = 200
# [5, 10, 15, 200, 25, 50, 20]

4.
list3 = []
odd = list1[1::2]
even = list2[0::2]
list3.extend(odd)
list3.extend(even)
# [6, 12, 18, 4, 12, 20, 28]
```

- Operators
  - Math: ```+ - * / % ** (Exponential) // (floor division)```
    - There alot more Math functions in the [Math module](https://www.w3schools.com/python/module_math.asp) and some [built into Python core](https://www.w3schools.com/python/python_math.asp)
  - Assignment: ```= += -= *= /=```
  - Comparison: ```== != > < >= <= in```
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
Fence Calculator - Posts and Railings
Create a script that can:
1) Calculate how many posts and railings are needed to build a fence of a certain length
2) Calculate the maximum length fence that can be created with any amount of posts and railings

Fences must meet the following spec:
A fence must consist of atleast 2 posts and 1 railing
Every railing must have a post before and after it
Posts cannot be place next to each other
Posts are 0.1m wide
Railings are 1.5m wide
When given a length, the calculator must create a fence that spans atleast that length

Stretch goals:
Display how many spare posts/railings there are when calculating the fence length
Display the overshoot when calculating how many posts and railings are needed for a fence length
```

#### ANSWER
```
import math

calcType = input('What kind of calculation do you want to do?'
                 '\n[1] Calculate the length of a fence'
                 '\n[2] Calculate how many posts and railings you will need\n')

print(calcType)

POST_LENGTH = 0.1
RAILING_LENGTH = 1.5

if calcType == "1":
    posts = input('How many posts do you have?\n')
    railings = input('How many railings do you have?\n')

    if posts > railings:
        fenceLength = round((int(railings) * (POST_LENGTH + RAILING_LENGTH)) + POST_LENGTH, 0)
        # You have to round as float maths is weird
    else:
        fenceLength = round(((int(railings)-1) * (POST_LENGTH + RAILING_LENGTH)) + POST_LENGTH, 0)
        # You have to round as float maths is weird
    print('Your fence will be: ' + str(fenceLength) + 'm')

elif calcType == "2":
    fenceLength = float(input('How Long does your fence need to be?\n'))

    if fenceLength < (POST_LENGTH + RAILING_LENGTH + POST_LENGTH):
        print("Fence must be over 1.6m")
    else:
        railings = math.ceil((fenceLength - POST_LENGTH) / RAILING_LENGTH)
        posts = railings + 1
        print("You will need " + str(railings) + " railings and " + str(posts) + " posts")

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
  
### EXERCISE
```
Write a short program that prints each number from 1 to 100 on a new line. 
For each multiple of 3, print "Fizz" instead of the number. 
For each multiple of 5, print "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
```

#### ANSWER
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
  - Arguments can be passed by specifying the param name: `func(param1 = "value")` often called `kwargs`
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

### EXERCISE
```
Create a function in a module that can take an unlimited amount of numbers 
and return the sum of those numbers, excluding negative numbers and numbers 
over 100.
``` 

#### ANSWER
```
def sum_positive(*numbers):
    filtered = []
    for number in numbers:
        if number > 0 and number <= 100:
            filtered.append(number)
    return sum(filtered)

# a better solution, students cant do yet:
def sum_positive(*numbers):
    return sum(filter(lambda a: a <= 100, filter(lambda a: a > 0, numbers)))
```

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
 
- Filtering
  - `filter()` function allows filtering of an iterable, you pass it a function and the data
  - The function should return `True` to include and `False` to exclude
  ```
  data = [5, 12, 3, 34, 54, 17]


  def is_odd(num):
    return (num % 2) == 1


  oddNumbers = list(filter(is_odd, data)) # cast to a list or you get an iterable which doesnt print well

  print(oddNumbers)
  ```
 
### EXERCISE
```
Output the names of the adults (18 and over) in age order (ASC):
people = [
    {"name": "Mike", "age": 28},
    {"name": "Jenny", "age": 12},
    {"name": "Sarah", "age": 21},
    {"name": "Robert", "age": 6},
    {"name": "Felix", "age": 41}
]
```

#### ANSWER
```
def is_adult(person):
    return person['age'] > 17


adults = list(filter(is_adult, people))


def sort_by_age(person):
    return person["age"]
    

adults.sort(key=sort_by_age)

for adult in adults:
    print(adult['name'])
    
# Sarah, Mike, Felix
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
  - Generally using the CSV library is not recommended, pandas is much easier. John will teach you more about working with pandas.
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
Create a module with the following functions:
- get_people_by_company
- get_person_by_id
Each function should query the database using the function parameter, and return the data

Use your functions to find:
- All the people who work for Babbleblab
- The person with id 65
```
#### ANSWER
```
# module
import pyodbc

conn = pyodbc.connect(
    server="localhost",
    database="test",
    user='sa',
    tds_version='7.4',
    password="Password123",
    port=1433,
    driver='/usr/local/lib/libtdsodbc.so'
)


def get_people_by_company(company):
    db = conn.cursor()
    db.execute('SELECT * FROM test.dbo.people WHERE company = ?', company)
    return db.fetchall()


def get_person_by_id(person_id):
    db = conn.cursor()
    db.execute('SELECT * FROM test.dbo.people WHERE id = ?', person_id)
    return db.fetchone()


# index

import module

people = module.get_people_by_company('Babbleblab')
print(people) 
# [
# (49, 'Marya', 'Behling', 'mbehling1c@npr.org', 'Babbleblab'), 
# (63, 'Cirstoforo', 'Wainer', 'cwainer1q@is.gd', 'Babbleblab'), 
# (73, 'Leigh', 'Werrilow', 'lwerrilow20@nsw.gov.au', 'Babbleblab')
# ]


person = module.get_person_by_id(65)
print(person) # (65, 'Daisy', 'Gravenall', 'dgravenall1s@twitpic.com', 'Thoughtbeat')
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



Additional exercise:

### EXERCISE
``` 
Blackjack
Write a blackjack like game. The game will randomly "draw" 4 cards, assign 2 to the player and 2 to the dealer. 
Calculate the score the player and the dealer got, the higher score wins, unless the score is over 21 in which 
case they "go bust" and the other player wins. If the scores are equal, it is a draw and neither player wins.
- Number cards are worth their numerical value
- Jack, Queen and King are worth 10
- Ace is worth 11
You must output the cards drawn by each player.
No card can be drawn more than once.

Stretch goal:
If the players score is under 21, ask them if they would like to draw another card. 
If they do, add the card value to their score. 
Allow the player to continue drawing cards until their score is 21 or they go bust.
```

#### ANSWER
[Blackjack](blackjack.py)
