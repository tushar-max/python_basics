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

### Exception Error

You want the program to detect errors, handle them, and then continue to run. Errors can be handled with try and except statements. The code that could potentially have an error is put in a try clause. The program execution moves to the start of a following except clause if an error happens.

You can put the previous divide-by-zero code in a try clause and have an except clause contain code to handle what happens when this error occurs.

    def spam(divideBy):
        try:
            return 42 / divideBy
        except ZeroDivisionError:
            print('Error: Invalid argument.')

    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))


