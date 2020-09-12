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