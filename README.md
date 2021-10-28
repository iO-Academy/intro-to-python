# Intro to Python

### Prep
- Make sure you have Python 3 installed (I will be using Python 3.9.6)
- Ensure you have a SQL (Mysql or MSSQL) database running
  - There is a [MSSQL Docker container](https://github.com/iO-Academy/intro-to-python/tree/docker) here for ease

## Programme

- What is Python?
  - Syntax
  - Modules
  - Comments
  - Best practice
  

- Variables
  - Cannot start with a number
  - Case-sensitive
  - Generally lowercase with underscores

- User input
  ```python3
  data = input("Message to prompt user")
  ```

- Data Types
  - Simple: `str`, `int`, `float`, `bool`, `None`
    - Concatenating
    - Casting
### EXERCISE
```python3
Write a script that asks the user for their name and age as 2 separate questions. 
Then print the following string with the correct data:
{name} will be {age} years old next year
```
  - Complex: `list`, `tuple`, `dict`, `set`
    - List
      - ```names = ['mike', 'charlie', 'ash']```
    - Tuple
        - ```names = ('mike', 'charlie', 'ash')``` 
    - Set: can make immutable with `frozenset()`
        - ```names = {'mike', 'charlie', 'ash'}```
    - Dictionary
        - ```person =	{"name": "Mike", "age": 28, "location": "Bath"}``` 

- Working with array types
  - [list](https://www.w3schools.com/python/python_lists_methods.asp)
    - Accessing
    - Editing
    - Removing
    - Slicing
  - [dict](https://www.w3schools.com/python/python_dictionaries_methods.asp)
    - Accessing
    - Methods
  
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

- 5. Stretch goal: add the list ["h", "i", "j"] after the "g" in the sub list of the following data:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
```
  
- Operators
  - Math: ```+ - * / % ** //```
    - [Python core](https://www.w3schools.com/python/python_math.asp)
    - [Math module](https://www.w3schools.com/python/module_math.asp) 
  - Assignment: ```= += -= *= /=```
  - Comparison: ```== != > < >= <= in```
  - Logical: ```and, or, not```

- Conditionals
  - if
  - elif
  - if ... else
  - Shorthand/ternary
 
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

- Loops
  - while
  - for
  - break
  - continue
  - else

### EXERCISE
```
Write a short program that prints each number from 1 to 100 on a new line. 
For each multiple of 3, print "Fizz" instead of the number. 
For each multiple of 5, print "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
```

- Functions
  - What are they for?
  - Syntax
    - PEP8
  - Args/Params
  - return
  - Lambda
  - Scope
  - Type Hinting
  
- Modules
  - What are they?
  - importing
  - aliasing
  - importing parts of a module
 
### EXERCISE
```
Create a function in a module that can take an unlimited amount of numbers 
and return the sum of those numbers, excluding negative numbers and numbers 
over 100.
``` 
 
 - [Sorting](https://www.w3schools.com/python/python_lists_sort.asp)
 - [Filtering](https://www.w3schools.com/python/ref_func_filter.asp)

### EXERCISE
```python3
# Output the names of the adults (18 and over) in age order (ASC):
people = [
    {"name": "Mike", "age": 28},
    {"name": "Jenny", "age": 12},
    {"name": "Sarah", "age": 21},
    {"name": "Robert", "age": 6},
    {"name": "Felix", "age": 41}
]
```

- Package manager: PIP
  - What is a package manager?
  - How to [find packages](https://pypi.org)
  - How to pick packages
  
- Working with files
  - Opening files
  - Reading data
  - Writing data
  - Closing files
  - Working with CSVs

- MSSQL
  - Connecting - `pyodbc`
  - Cursor
  - Running queries
    - fetchall
    - fetchone
  - Prepared statements
  - Running mulitple queries
  
### EXERCISE
Use [this database](people.sql)
```
Create a module with the following functions:
- get_people_by_company
- get_person_by_id
Each function should query the database using the function parameter, and return the data

Use your functions to find:
- All the people who work for Babbleblab
- The person with id 65
```

- OO Python
  - What is OO?
  - What is a class?
  - Syntax
  
Additional reading:
  - [W3Schools](https://www.w3schools.com/python/default.asp)
  - [Python Exercises](https://pynative.com/python-exercises-with-solutions/)
  - [Real Python](https://realpython.com/)
  - [Learn Python](https://www.learnpython.org/)
  - [Python Docs](https://docs.python.org/3/)
  
Additional Exercise:
  
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
If the players score is under 14, ask them if they would like to draw another card. 
If they do, add the card value to their score. 
Allow the player to continue drawing cards until their score is 21 or they go bust.
```
