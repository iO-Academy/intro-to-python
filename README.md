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
  - Simple: str, ing, float, bool
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
  - Scope
  - https://www.w3schools.com/python/python_variables_global.asp
  
- Sorting

  
### EXERCISE
``` 
Blackjack
```
#### ANSWER
```

```
