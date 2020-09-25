### Raising Exceptions

Python raises an exception whenever it tries to execute invalid code. 

Raising an exception is a way of saying, **“Stop running the code in this function and move the program execution to the except statement."**

Exceptions are raised with a raise statement. In code, a raise statement consists of the following:

The raise keyword

* A call to the Exception() function
* A string with a helpful error message passed to the Exception() function
* For example, enter the following into the interactive shell:

    >>> raise Exception('This is the error message.')
    Traceback (most recent call last):
    File "<pyshell#191>", line 1, in <module>
        raise Exception('This is the error message.')
    Exception: This is the error message.

### Traceback

Python displays the traceback whenever a raised exception goes unhandled. But you can also obtain it as a string by calling traceback.format_exc(). This function is useful if you want the information from an exception’s traceback but also want an except statement to gracefully handle the exception. You will need to import Python’s traceback module before calling this function.

For example, instead of crashing your program right when an exception occurs, you can write the traceback information to a text file and keep your program running.

    >>> import traceback
    >>> try:
    ...          raise Exception('This is the error message.')
    except:
    ...          errorFile = open('errorInfo.txt', 'w')
    ...          errorFile.write(traceback.format_exc())
    ...          errorFile.close()
    ...          print('The traceback info was written to errorInfo.txt.')

### Assertions

An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. 

An assert statement consists of the following:

* The assert keyword
* A condition (that is, an expression that evaluates to True or False)
* A comma
* A string to display when the condition is False

**“I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program.”**

    >>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
    >>> ages.reverse()
    >>> ages
    [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
    >>> assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AssertionError

Unlike exceptions, your code should not handle assert statements with try and except; if an assert fails, your program should crash. 

### Logging
If you’ve ever put a print() statement in your code to output some variable’s value while your program is running, you’ve used a form of logging to debug your code. Logging is a great way to understand what’s happening in your program and in what order it’s happening. Python’s logging module makes it easy to create a record of custom messages that you write. These log messages will describe when the program execution has reached the logging function call and list any variables you have specified at that point in time. 

    import logging
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)
    s -  %(message)s')  
    logging.debug('Start of program')

    def factorial(n):
        logging.debug('Start of factorial(%s%%)'  % (n))
        total = 1
        for i in range(n + 1):
            total *= i
            logging.debug('i is ' + str(i) + ', total is ' + str(total))
        logging.debug('End of factorial(%s%%)'  % (n))
        return total

    print(factorial(5))
    logging.debug('End of program')