
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

### List Concatenation and List Replication

Lists can be concatenated and replicated just like strings. The + operator combines two lists to create a new list value and the * operator can be used with a list and an integer value to replicate the list.

    >>> [1, 2, 3] + ['A', 'B', 'C']
    [1, 2, 3, 'A', 'B', 'C']
    >>> ['X', 'Y', 'Z'] * 3
    ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

### The Multiple Assignment Trick

The multiple assignment trick (technically called tuple unpacking) is a shortcut that lets you assign multiple variables with the values in a list in one line of code.

    >>> cat = ['fat', 'gray', 'loud']
    >>> size, color, disposition = cat

### enumerate() function

Instead of using the range(len(someList)) technique with a for loop to obtain the integer index of the items in the list, you can call the enumerate() function instead. On each iteration of the loop, enumerate() will return two values: the index of the item in the list, and the item in the list itself.

    >>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
    >>> for index, item in enumerate(supplies):
    ...     print('Index ' + str(index) + ' in supplies is: ' + item)

    Index 0 in supplies is: pens
    Index 1 in supplies is: staplers
    Index 2 in supplies is: flamethrowers
    Index 3 in supplies is: binders

**The enumerate() function is useful if you need both the item and the item’s index in the loop’s block.**

### random.choice() and random.shuffle()

* The random.choice() function will return a randomly selected item from the list
* The random.shuffle() function will reorder the items in a list.

        >>> import random
        >>> people = ['Alice', 'Bob', 'Carol', 'David']
        >>> random.shuffle(people)
        >>> people
        ['Carol', 'David', 'Alice', 'Bob']
        >>> random.shuffle(people)
        >>> people
        ['Alice', 'David', 'Bob', 'Carol']

### Removing Values from Lists with del Statements

The del statement will delete values at an index in a list. All of the values in the list after the deleted value will be moved up one index.

    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> del spam[2]
    >>> spam
    ['cat', 'bat', 'elephant']

The del statement can also be used on a simple variable to delete it, as if it were an “unassignment” statement.

### Methods

A method is the same thing as a function, except it is “called on” a value. For example, if a list value were stored in spam, you would call the index() list method (which I’ll explain shortly) on that list like so: spam.index('hello'). The method part comes after the value, separated by a period.

#### Methods List

* .index("foo") - Ill return the index of the first apperance of the value
* .append("bar") - Ill add to the final of the list the value "bar"
* .insert(1,"fo") - Ill add at the index 1 the value "fo"

        >>> spam = ['cat', 'dog', 'bat']
        >>> spam.insert(1, 'chicken')
        >>> spam
        ['cat', 'chicken', 'dog', 'bat']

* .remove("foo") - Ill remove the value "foo" from the list. The **del statement** is good to use when you know the index of the value you want to remove from the list. The remove() method is useful when you know the value you want to remove from the list.
* .sort() - Lists of number values or lists of strings can be sorted with the sort() method. You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order.
    * If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call.

            >>> spam = ['a', 'z', 'A', 'Z']
            >>> spam.sort(key=str.lower)
            >>> spam
            ['a', 'A', 'z', 'Z']

* .reverse() - If you need to quickly reverse the order of the items in a list

### Exceptions to Indentation rules in python

You can split up a single instruction across multiple lines using the \ line continuation character at the end. Think of \ as saying, “This instruction continues on the next line.” The indentation on the line after a \ line continuation is not significant. For example, the following is valid Python code:

    print('Four score and seven ' + \
        'years ago...')

These tricks are useful when you want to **rearrange long lines of Python code** to be a bit more readable.


### Tuple Data Type

The tuple data type is almost identical to the list data type, except in two ways. First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ]. And Tuples cannot have their values modified, appended, or removed.

If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses. Otherwise, Python will think you’ve just typed a value inside regular parentheses. The comma is what lets Python know this is a tuple value.

    >>> type(('hello',))
    <class 'tuple'>

A benefit of using tuples instead of lists is that, because they are immutable and their contents don’t change, Python can implement some optimizations that make code **using tuples slightly faster than code using lists.**

### list() and tuple() functions

The functions list() and tuple() will return list and tuple versions of the values passed to them.

### The id() Function

All values in Python have a unique identity that can be obtained with the id() function.

When Python runs id('Howdy'), it creates the 'Howdy' string in the computer’s memory. The numeric memory address where the string is stored is returned by the id() function. Python picks this address based on which memory bytes happen to be free on your computer at the time, so it’ll be different each time you run this code.

If two variables refer to the same list (like spam and cheese in the previous section) and the list value itself changes, both variables are affected because they both refer to the same list. The append(), extend(), remove(), sort(), reverse(), **and other list methods modify their lists in place.**

### Copy Module - copy() and deepcopy() functions

Although passing around references is often the handiest way to deal with lists and dictionaries, if the function modifies the list or dictionary that is passed, you may not want these changes in the original list or dictionary value. For this, Python provides a module named copy that provides both the copy() and deepcopy() functions. The first of these, copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.

    >>> import copy
    >>> spam = ['A', 'B', 'C', 'D']
    >>> id(spam)
    44684232
    >>> cheese = copy.copy(spam)
    >>> id(cheese) # cheese is a different list with different identity.
    44685832
    >>> cheese[1] = 42
    >>> spam
    ['A', 'B', 'C', 'D']
    >>> cheese
    ['A', 42, 'C', 'D']

Now the spam and cheese variables refer to separate lists, which is why only the list in cheese is modified when you assign 42 at index 1.

If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy(). **The deepcopy() function will copy these inner lists as well.**

### Dictionary Data Type

Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair.

    >>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
    >>> myCat['size']
    'fat'

Dictionaries can still use **integer values as keys**, just like lists use integers for indexes, but they do not have to start at 0 and can be any number.

    >>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}

### The keys(), values(), and items() Methods

There are three dictionary methods that will return list-like values of the dictionary’s keys, values, or both keys and values: keys(), values(), and items(). The values returned by these methods are not true lists: they cannot be modified and do not have an append() method. But these data types (dict_keys, dict_values, and dict_items, respectively) can be used in 
for loops. 

    >>> spam = {'color': 'red', 'age': 42}
    >>> for v in spam.values():
    ...     print(v)
    # red
    # 42

    >>> for k in spam.keys():
    ...     print(k)
    # color
    # age

    >>> for i in spam.items():
    ...     print(i)
    # ('color', 'red')
    # ('age', 42)

    >>> spam = {'color': 'red', 'age': 42}
    >>> for k, v in spam.items():
    ...     print('Key: ' + k + ' Value: ' + str(v))
    # Key: age Value: 42
    # Key: color Value: red

### get() Method

Dictionaries have a get() method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist.

### setfdefault() Method

The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key does not exist. If the key does exist, the setdefault() method returns the key’s value.

    >>> spam = {'name': 'Pooka', 'age': 5}
    >>> spam.setdefault('color', 'black')
    'black'
    >>> spam
    {'color': 'black', 'age': 5, 'name': 'Pooka'}
    >>> spam.setdefault('color', 'white')
    'black'
    >>> spam
    {'color': 'black', 'age': 5, 'name': 'Pooka'}

### Escape Character

| Escape Character | Prints as |
| --- | --- |
| \'  | Single Quote |
| \"  | Double Quote |
| \t  | Tab  |
| \n  | Newline(line break) |
| \\  | Backslash  | 


### Raw Strings

You can place an r before the beginning quotation mark of a string to make it a raw string. A raw string completely ignores all escape characters and prints any backslash that appears in the string. 

    >>> print(r'That is Carol\'s cat.')
    That is Carol\'s cat.

Raw strings are helpful if you are typing string values that contain many backslashes, such as the strings used for Windows file paths like r'C:\Users\Al\Desktop' 


### The isX() Methods

* isalpha() Returns True if the string consists only of letters and isn’t blank
* isalnum() Returns True if the string consists only of letters and numbers and is not blank
* isdecimal() Returns True if the string consists only of numeric characters and is not blank
* isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
* istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters

### The startswith() and endswith() Methods

The startswith() and endswith() methods return True if the string value they are called on begins or ends (respectively) with the string passed to the method; otherwise, they return False. Enter the following into the interactive shell:

    >>> 'Hello, world!'.startswith('Hello')
    True
    >>> 'Hello, world!'.endswith('world!')
    True

### join() and split() Mehtods

The join() method is useful when you have a list of strings that need to be joined together into a single string value. The join() method is called on a string, gets passed a list of strings, and returns a string.

    >>> ', '.join(['cats', 'rats', 'bats'])
    'cats, rats, bats'
    >>> ' '.join(['My', 'name', 'is', 'Simon'])
    'My name is Simon'

The split() method does the opposite: It’s called on a string value and returns a list of strings. 

### Splitting Strings with the partition() method

The partition() string method can split a string into the text before and after a separator string. This method searches the string it is called on for the separator string it is passed, and returns a tuple of three substrings for the “before,” “separator,” and “after” substrings.

    >>> 'Hello, world!'.partition('w')
    ('Hello, ', 'w', 'orld!')
    >>> 'Hello, world!'.partition('world')
    ('Hello, ', 'world', '!')

If the separator string you pass to partition() occurs multiple times in the string that partition() calls on, the method splits the string only on the first occurrence.

### Removing Whitespace with the strip()

The strip() string method will return a new string without any whitespace characters at the beginning or end. 

    >>> spam = '    Hello, World    '
    >>> spam.strip()
    'Hello, World'

Optionally, a string argument will specify which characters on the ends should be stripped. Enter the following into the interactive shell:

    >>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
    >>> spam.strip('ampS')
    'BaconSpamEggs'

Passing strip() the argument 'ampS' will tell it to strip occurrences of a, m, p, and capital S from the ends of the string stored in spam. The order of the characters in the string passed to strip() does not matter: strip('ampS') will do the same thing as strip('mapS') or strip('Spam').

### ord() and chr() methods

You can use the ord() function to get the code point of a one-character string, and the chr() function to get the one-character string of an integer code point.

    >>> ord('!')
    33
    >>> chr(65)
    'A'

### Copying and Pasting Strings with the pyperclip Module

The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard. Sending the output of your program to the clipboard will make it easy to paste it into an email, word processor, or some other software.

    >>> import pyperclip
    >>> pyperclip.copy('Hello, world!')
    >>> pyperclip.paste()
    'Hello, world!'

### Running script out of the IDLE

On Windows, you can create a batch file to run this program with the WIN-R Run window. (For more about batch files, see Appendix B.) Enter the following into the file editor and save the file as mclip.bat in the C:\Windows folder:

@py.exe C:\path_to_file\mclip.py %*
@pause

With this batch file created, running the multi-clipboard program on Windows is just a matter of pressing WIN-R and typing mclip key phrase.


### Regular Expressions (Regex)

See file automate_boring_stuff\exercicies\regex.py

While there are several steps to using regular expressions in Python, each step is fairly simple.

Import the regex module with import re.
Create a Regex object with the re.compile() function. (Remember to use a raw string.)
Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
Call the Match object’s group() method to return a string of the actual matched text.

The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters. In regular expressions, the following characters have special meanings:

    .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )

You can think of the ? as saying, “Match zero or one of the group preceding this question mark.”

While * means “match zero or more,” the + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once. 

Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy (also called lazy) version of the braces, which matches the shortest string possible, has the closing brace followed by a question mark.

    >>> greedyHaRegex = re.compile(r'(Ha){3,5}')
    >>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
    >>> mo1.group()
    'HaHaHaHaHa'

    >>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
    >>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
    >>> mo2.group()
    'HaHaHa'

Note that the question mark can have two meanings in regular expressions: declaring a non-greedy match or flagging an optional group. These meanings are entirely unrelated.

#### findall() Method

To summarize what the findall() method returns, remember the following:

* When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].
* When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), the method findall() returns a list of tuples of strings (one string for each group), such as [('415', '555', '9999'), ('212', '555', '0000')].

### Character Classes

![characther_class](/automate_boring_stuff\images\characters_class.png)

The character class [0-5] will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5). Note that while \d matches digits and \w matches digits, letters, and the underscore, there is no shorthand character class that matches only letters. (Though you can use the [a-zA-Z] character class, as explained next.)

You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

Note that inside the square brackets, the normal regular expression symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or () characters with a preceding backslash.

By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class.

You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.

I always confuse the meanings of these two symbols, so I use the mnemonic “Carrots cost dollars” to remind myself that the caret comes first and the dollar sign comes last.

The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

#### Matching Everything with Dot-Star

Sometimes you will want to match everything and anything. For example, say you want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and then followed by anything again. You can use the dot-star (.*) to stand in for that “anything.”

    >>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    >>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
    >>> mo.group(1)
    'Al'
    >>> mo.group(2)
    'Sweigart'

#### Matching Newlines with the Dot Character

The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.

    >>> newlineRegex = re.compile('.*', re.DOTALL)
    >>> newlineRegex.search('Serve the public trust.\nProtect the innocent.
    \nUphold the law.').group()
    'Serve the public trust.\nProtect the innocent.\nUphold the law.'

#### Review of Regex Symbols

This chapter covered a lot of notation, so here’s a quick review of what you learned about basic regular expression syntax:

* The ? matches zero or one of the preceding group.
* The * matches zero or more of the preceding group.
* The + matches one or more of the preceding group.
* The {n} matches exactly n of the preceding group.
* The {n,} matches n or more of the preceding group.
* The {,m} matches 0 to m of the preceding group.
* The {n,m} matches at least n and at most m of the preceding group.
* {n,m}? or *? or +? performs a non-greedy match of the preceding group.
* ^spam means the string must begin with spam.
* spam$ means the string must end with spam.
* The . matches any character, except newline characters.
* \d, \w, and \s match a digit, word, or space character, respectively.
* \D, \W, and \S match anything except a digit, word, or space character, respectively.
* [abc] matches any character between the brackets (such as a, b, or c).
* [^abc] matches any character that isn’t between the brackets.

#### Case-Insensitive Matching

But sometimes you care only about matching the letters without worrying whether they’re uppercase or lowercase. To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile(). 

    >>> robocop = re.compile(r'robocop', re.I)

#### The sub() Method

The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.

    >>> namesRegex = re.compile(r'Agent \w+')
    >>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
    'CENSORED gave the secret documents to CENSORED.'

Sometimes you may need to use the matched text itself as part of the substitution. In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”

    >>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
    >>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
    Eve knew Agent Bob was a double agent.')
    A**** told C**** that E**** knew B**** was a double agent.'

#### Managing Complex Regexes

You can spread the regular expression over multiple lines with comments like this:

    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?            # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)                     # separator
        \d{4}                         # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
        )''', re.VERBOSE)

#### Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

Including all three options in the second argument will look like this:

    >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

