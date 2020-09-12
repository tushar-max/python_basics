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

### The in and not in Operators

You can determine whether a value is or isn’t in a list with the in and not in operators. Like other operators, in and not in are used in expressions and connect two values: a value to look for in a list and the list where it may be found. These expressions will evaluate to a Boolean value. 

    >>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
    True
    >>> spam = {'name': 'Zophie', 'age': 7}
    >>> 'name' in spam.keys()
    True
    >>> 'Zophie' in spam.values()
    True
    >>> 'color' in spam
    False

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
    >>> print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    >>> print('Hello', end='')
    >>> print('cats', 'dogs', 'mice', sep=',')
    cats,dogs,mice