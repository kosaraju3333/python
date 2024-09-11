**Python For DevOps: Guide for DevOps Engineers**

- https://devopscube.com/python-for-devops/

Python is a **DYNAMIC TYPED** program 

**`Day-01:`**

Why Python

1: Use for both Linux and windows machines 

2: When you want to write complex ,interact with api’s, data manipulation and ect…

**`Day-02:`**

Introduction to Python Data Types

In programming, a data type is a classification or categorization that specifies which type of value a variable can hold. Data types are essential because they determine how data is stored in memory and what operations can be performed on that data. Python, like many programming languages, supports several built-in data types. Here are some of the common data types in Python:

1. **Numeric Data Types:**
    - **int**: Represents integers (whole numbers). Example: `x = 5`
    - **float**: Represents floating-point numbers (numbers with decimal points). Example: `y = 3.14`
    - **complex**: Represents complex numbers. Example: `z = 2 + 3j`
2. **Sequence Types:**
    - **str**: Represents strings (sequences of characters). Example: `text = "Hello, World"`
    - **list**: Represents lists (ordered, mutable sequences). Example: `my_list = [1, 2, 3]`
    - **tuple**: Represents tuples (ordered, immutable sequences). Example: `my_tuple = (1, 2, 3)`
3. **Mapping Type:**
    - **dict**: Represents dictionaries (key-value pairs). Example: `my_dict = {'name': 'John', 'age': 30}`
4. **Set Types:**
    - **set**: Represents sets (unordered collections of unique elements). Example: `my_set = {1, 2, 3}`
    - **frozenset**: Represents immutable sets. Example: `my_frozenset = frozenset([1, 2, 3])`
5. **Boolean Type:**
    - **bool**: Represents Boolean values (`True` or `False`). Example: `is_valid = True`
6. **Binary Types:**
    - **bytes**: Represents immutable sequences of bytes. Example: `data = b'Hello'`
    - **bytearray**: Represents mutable sequences of bytes. Example: `data = bytearray(b'Hello')`
7. **None Type:**
    - **NoneType**: Represents the `None` object, which is used to indicate the absence of a value or a null value.
8. **Custom Data Types:**
    - You can also define your custom data types using classes and objects.

**`Day-03:`**

keywords and Variables.

1: Keywords 

- https://github.com/kosaraju3333/python-for-devops/blob/main/Day-03/keywords.md

2: Variables:

Global and Local

Naming conversions 

**Note : 3 Rules for Variables Naming** conversions

- **Always declare variables in lower case only**
- **Snake(full_name) or Camel(FullName) casing**
- **As Descriptive as descriptive.**
- https://github.com/kosaraju3333/python-for-devops/blob/main/Day-03/variables.md

**`Day-04:`**

Functions, Modules and Packages. 

Functions Advantages:

- Redability
- Re-usability (Modularity)
- Debugging

**Functions**

- Takes the  input
- perform the required action
- Return the output.

**Modules:** 

Re-usability 

**Module is a GROUP of FUNCTIONS** 

**Packages :**

- **Collection of Modules( collection of python files ).**

**Virtual Environment**

If you are using Same VM for multiple projects, then if you have to use same package with different version for different projects then we can you Virtual Environment  in python

- pip install virtualenv
- python -m venv project-name
- source project-name/bin/activate
- decativate to come out from
- Logical separation  for packages

**`Day-05:`**

Command Line arguments and Environment Variables

1: Command Line arguments

- Command Line arguments are used to pass the values to your program as input.
- To read Command line argument you need use **SYS** module it is in-build module no need to install.
- **Note : By default arguments read as string in python.**
    
    ```jsx
    sys.argv[0 or 1 or 2 etc..]
    ```
    

2 : Environment Variables (env vars)

Note: To read a Environment variables you need to import **`OS`** module 

```jsx
os.getenv(”env_var_name”)
```

- TO deal with sensitive information you need to use environment variables.
    - eg of sensitive information
        - Passwords
        - API keys
        - TOKENS
        - Certificates and etc..
        

**`Day-06:`**

Operators

- Arithmetic Operator:
    
    ```jsx
    a + b
    a - b
    a * b
    a / b (Division) eg: 16/13 = 1.2
    a // b (Floor Divison) eg: 16/13 = 1
    a % b (Modules (Remainder)) eg: 16/13 = 3
    ```
    

- Assignment Operator:
    
    ```jsx
    a = 1
    a = a + 3 or a+ = 3 (Both are same called as Addition assignment)
    						AND
    a = 2
    a = a - 1 or a- = 1 (Both are same)
    ```
    
- Bitwise Operators
- Identity Operators:
    
    ```jsx
    a = 5
    b = 5
    a is b -> output is TRUE
    a is not b -> output is FALSE
    ```
    
- Logical Operators:
    - 
    
    ```jsx
    AND
    	T AND T = T
    	T AND F = F
    	F AND T = F
    	F AND F = F
    OR
    	T OR T = T
    	T OR F = T
    	F OR T = T
    	F OR F = F
    NOR
    ```
    
- Relational Operators:
    
    ```jsx
    a > b
    a < b
    a >= b
    a <= b
    a == b
    
    ```
    

**`Day-07`**

Conditional Handling  (if, elif and else) 

It will handle a particular condition 

- if - For to check 2 conditions
- elif - FOR to check more than 2 conditions.
- else

**`Day-08`**

Basics of **Lists and Tuples: (Sequence datatype)**

Why to use Lists and Tuples

- Lists:
    - If you want to store multiple variables in a single variable you can use lists
    - Lists are **MUTUBLE**
    - Lits has dynamic memory allocation.
    - List can be created with different datatypes as well
        - List are Heterogeneous in nature
        
        ```jsx
        eg: random_list = 1, 2, 3, "RAM", "KRISH", 7.5]
        ```
        
        - List Example
            - List functions
                - append
                - remove
                - length
                - slicing —> (Upper bound will not print)
                - sort
                - Concatenating
        
        ```jsx
        eg: student_names = [”RAM”, “KRISH”, ”RAMKI”,……etc..]
        		print(student_names)
        		print(student_names[0])
         
        		student_names.append("name")
        		student_names.remove("name")
        		len(student_names)
        ```
        
- Tuples:
    - Tuples are **IMMUTUBLE**
    - Tuples are not modified **MODIFIED**  or not **RESIZED (CAN NOT ADD or REMOVED)**
    - Tuples has better memory footprints.
        - 
        
        ```jsx
        eg: aws_admin_users = ("RAM", "KRISH")
        		print(aws_admin_users)
        ```
        
    

**`Day-09:`**

Loops:

- If you want to perform a repetitive action on a block of code then we use LOOPS.

1: FOR Loop:

- When you know that you need to execute a particular block of statements for a definite number of times (When you clearly know that you have to execute block of code 1,23,20,1000 or 1M times or a specific number of times then we will use FOR loops)
    - Syntax
    
    ```jsx
    for i(any_variable) in sequence:
    
    sequence mainly use **range, lists, tuples**
    ```
    

2: WHILE Loop:

- When you are not sure or when there is no definite number of times of execution of block of code then we go with WHILE loop. (When you don’t know the number of executions of code block. )
    - Syntax
    
    ```jsx
    while condition:
    ```
    

3: Loop Manapulation:

1: break

- I will break the loop if the condition is matched

2: continue 

- I will skip the current loop iteration and go to the next iteration.

**`Day-10:`**

Working With Lists PART-2 (Advanced)

Basic of LISTS in DAY-08

**`DAY-11`:**

Dictionaries and Sets Data types.

**Dictionaries:**

- Store the properties of the info in KEY-VALUE pair.
    - 
    
    ```jsx
    eg: Storing RAM Student properties/info 
    
    student_info = {
    				"name"   : "RAM",
    				"age"    : 14,
    				"class"  : 10
    				"roll_No" : 62
    			}
    to print student name from dictionarie
    print(student_info["name"])
    ```
    

Sets:

- set has uniq elements (NO Duplicates)
- Some example : Store the S3 bucket names because S3 bucket names has to be UNIQ

**`Day-12:`**

**File Operations:**

- When you want to read, update, delete in python, in that case you need FILE OPERATIONS
- There are 2 FILE OPERATIONS
    - read operation
    - write operation

**`Day-13:`**

**Boto3:**

**Lambda Functions:** 

**`Day-14:`**

Real time project.

**`Day-15:`**

API:

- API works on HTTP request types:
    - POST
    - GET
    - PUT
    - DELETE

convert python to API

FLASK:

- FLASK need a Decarative  for a function to route (@app.route(”path”) )
- FLASK creates an inbuild server [app.run(’0.0.0.0’)]
