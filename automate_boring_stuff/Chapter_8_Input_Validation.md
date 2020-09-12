### The PyInputPlus Module

PyInputPlus contains functions similar to input() for several kinds of data: numbers, dates, email addresses, and more. If the user ever enters invalid input, such as a badly formatted date or a number that is outside of an intended range, PyInputPlus will reprompt them for input.

If no errors appear when you import the module, it has been successfully installed.

PyInputPlus has several functions for different kinds of input:

* inputStr() Is like the built-in input() function but has the general PyInputPlus features. You can also pass a custom validation function to it
* inputNum() Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it
* inputChoice() Ensures the user enters one of the provided choices
* inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options
* inputDatetime() Ensures the user enters a date and time
* inputYesNo() Ensures the user enters a “yes” or “no” response
* inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value
* inputEmail() Ensures the user enters a valid email address
* inputFilepath() Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists
* inputPassword() Is like the built-in input(), but displays * characters as the user types so that passwords, or other sensitive information, aren’t displayed on the screen

        >>> import pyinputplus as pyip
        >>> response = pyip.inputNum()
        five
        'five' is not a number.
        42
        >>> response
        42

If you take a look at the example, you see that unlike input(), these functions return an int or float value: 42 and 3.14 instead of the strings '42' and '3.14'.


### The min, max, greaterThan, and lessThan Keyword Arguments

The inputNum(), inputInt(), and inputFloat() functions, which accept int and float numbers, also have min, max, greaterThan, and lessThan keyword arguments for specifying a range of valid values.

    >>> response = pyip.inputNum('Enter num: ', min=4)
    Enter num:3
    Input must be at minimum 4.
    Enter num:4
    >>> response
    4

### The blank Keyword Argument

By default, blank input isn’t allowed unless the blank keyword argument is set to True:

    >>> response = pyip.inputNum(blank=True)
    (blank input entered here)
    >>> response
    ''

### The limit, timeout, and default Keyword Arguments

 Pass an integer for the limit keyword argument to determine how many attempts a PyInputPlus function will make to receive valid input before giving up, and pass an integer for the timeout keyword argument to determine how many seconds the user has to enter valid input before the PyInputPlus function gives up.

    >>> response = pyip.inputNum(timeout=10)
    >>> response = pyip.inputNum(limit=2)

### The allowRegexes and blockRegexes Keyword Arguments

    >>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

### Passing a Custom Validation Function to inputCustom()

we can create our own addsUpToTen() function, and then pass it to inputCustom(). Note that the function call looks like inputCustom(addsUpToTen) and not inputCustom(addsUpToTen()) because we are passing the addsUpToTen() function itself to inputCustom(), not calling addsUpToTen() and passing its return value.

