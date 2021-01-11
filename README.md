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
  - 
  ```
  age = 28
  name, age, location = "Mike", 28, "Bath"
  ```
 - Must start with a letter or the underscore character 
 - Cannot start with a number
 - Alpha-numeric characters and underscores (A-z, 0-9, and _ )
 - Case-sensitive
 - Generally lowercase with underscores
- Constants?

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
        





- Operators

- Conditionals
  - if
  - if ... else
 
- Functions
  - Scope
  - https://www.w3schools.com/python/python_variables_global.asp
  
