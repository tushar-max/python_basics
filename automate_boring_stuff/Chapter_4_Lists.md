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