# Intro to Python

- What is Python?
  - Syntax
    - Whitespace (spaces not tabs). Python is a whitespace based language, this means it defines blocks of code using indentation, or whitespace, rather than by using brackets. Most languages are either bracket based or whitespace based, in order to define different blocks of code.
  - Best practice
    - Python Enhancement Proposals (PEPs)
    - https://www.python.org/dev/peps/
    - [Code style](https://www.python.org/dev/peps/pep-0008/) 
  - Comments
    - Single line `#`
    - Multi-line `"""comment here"""` - not used
  
- Variables
  - Used for storing variable data, this means data that can change.  
  ```
  age = 28
  name, age, location = "Mike", 28, "Bath"
  ```
  - Must start with a letter or the underscore character 
  - Cannot start with a number
  - Alpha-numeric characters and underscores (A-z, 0-9, and _ )
  - Case-sensitive
  - Generally lowercase with underscores

- Data Types
  - Simple: str, ing, float, bool
  - Other:
    - [range](https://www.w3schools.com/python/ref_func_range.asp): a list of numbers starting from 0
    - EXERCISE
  - Complex: list, tuple, dict, set
    - 4 data types that allow for storing multiple values (array), all can contain any data type
      - list: ordered, changeable, 0 indexed, allows dups 
        - ```names = ['mike', 'charlie', 'ash']```
      - Tuple: ordered, unchangeable, 0 indexed, allows dups
        - ```names = ('mike', 'charlie', 'ash')``` 
      - Set: unordered, unindexed, unchangeable, no dups, *can add new items*, can make immutable with `frozenset()`
        - ```names = {'mike', 'charlie', 'ash'}```
      - Dictionary: unordered, changeable, no dup keys
        - ```person =	{"name": "Mike", "age": 28, "location": "Bath"}```       
    - EXERCISE - using array types
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
  
EXERCISE?

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
  
