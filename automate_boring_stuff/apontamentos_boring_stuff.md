
## Introduction

### Math Operators

Table 1-1: Math Operators from Highest to Lowest Precedence

![math_operators](/automate_boring_stuff\images\table1_math_operators.png)

>The order of operations (also called precedence) of Python math operators is similar to that of mathematics. The ** operator is evaluated first; the *, /, //, and % operators are evaluated next, from left to right; and the + and - operators are evaluated last (also from left to right).

### Variable Names

You can name a variable anything as long as it obeys the following three rules:

* It can be only one word with no spaces.
* It can use only letters, numbers, and the underscore (_) character.
* It can’t begin with a number.

Though Spam is a valid variable you can use in a program, it is a Python convention to start your variables with a lowercase letter.

### The input() function

The input() function waits for the user to type some text on the keyboard and press ENTER.

This function call evaluates to a string equal to the user’s text, and the line of code assigns the myName variable to this string value.

### str() int() and float()

The str(), int(), and float() functions will evaluate to the string, integer, and floating-point forms of the value you pass, respectively.

### Comparison Operators

Comparison operators, also called relational operators, compare two values and evaluate down to a single Boolean value. Table 2-1 lists the comparison operators.

![comparison_operators_boolean](/automate_boring_stuff\images\table2_comparison_operators.png)

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or expression). This makes it a unary operator. The not operator simply evaluates to the opposite Boolean value.

    >>> not True
    False
    >>> not not not not True
    True

### “TRUTHY” AND “FALSEY” VALUES

Conditions will consider some values in other data types equivalent to True and False. When used in conditions, 0, 0.0, and **'' (the empty string) are considered False**, while all other values are considered True.

### Statements Loops

#### Break

There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains the break keyword.

#### Continue

Like break statements, continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. (This is also what happens when the execution reaches the end of the loop.)

### The range() function

The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.

### Import Modules

Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:

* The import keyword
* The name of the module
* Optionally, more module names, as long as they are separated by commas

        import random, sys, os, math
        for i in range(5):
            print(random.randint(1, 10))


The random.randint() function call evaluates to a random integer value between the two integers that you pass it. Since randint() is in the random module, you must first type random. in front of the function name to tell Python to look for this function inside the random module.

#### sys.exit()

You can cause the program to terminate, or exit, before the last instruction by calling the sys.exit() function. Since this function is in the sys module, you have to import sys before your program can use it.

### Print() function

The print() function has the optional parameters end and sep to specify what should be printed at the end of its arguments and between its arguments (separating them), respectively.

    >>> print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    >>> print('Hello', end='')
    >>> print('cats', 'dogs', 'mice', sep=',')
    cats,dogs,mice

### Functions

A value being passed to a function in a function call is an argument.Variables that have arguments assigned to them are parameters.

Behind the scenes, Python adds return None to the end of any function definition with no return statement. This is similar to how a while or for loop implicitly ends with a continue statement. Also, if you use a return statement without a value (that is, just the return keyword by itself), then None is returned.

    >>> spam = print('Hello!')
    Hello!
    >>> None == spam
    True

#### The Global Statement

If you need to modify a global variable from within a function, use the global statement. If you have a line such as global eggs at the top of a function, it tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.” For example, enter the following code into the file editor and save it as globalStatement.py:

    def spam():
    ➊ global eggs
    ➋ eggs = 'spam'

    eggs = 'global'
    spam()
    print(eggs)

When you run this program, the final print() call will output this:

    spam

There are four rules to tell whether a variable is in a local scope or global scope:

* If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
* If there is a global statement for that variable in a function, it is a global variable.
* Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
* But if the variable is not used in an assignment statement, it is a global variable.

If you try to use a local variable in a function before you assign a value to it, as in the following program, Python will give you an error. 

    def spam():
        print(eggs) # ERROR!
        eggs = 'spam local'

    eggs = 'global'
    spam()

This error happens because Python sees that there is an assignment statement for eggs in the spam() function ➊ and, therefore, considers eggs to be local. But because print(eggs) is executed before eggs is assigned anything, the local variable eggs doesn’t exist. Python will not fall back to using the global eggs variable ➋.