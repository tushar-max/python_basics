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