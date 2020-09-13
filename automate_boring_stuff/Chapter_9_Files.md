### Files and File Paths

A file has two key properties: a filename (usually written as one word) and a path. The path specifies the location of a file on the computer. 

The C:\ part of the path is the root folder, which contains all other folders. On Windows, the root folder is named C:\ and is also called the C: drive.

On Windows, paths are written using backslashes (\) as the separator between folder names. 

If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases.

Fortunately, this is simple to do with the Path() function in the pathlib module. If you pass it the string values of individual file and folder names in your path, Path() will return a string with a file path using the correct path separators. 

    >>> from pathlib import Path
    >>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
    >>> for filename in myFiles:
            print(Path(r'C:\Users\Al', filename))
    C:\Users\Al\accounts.txt
    C:\Users\Al\details.csv
    C:\Users\Al\invite.docx


So while Path(r'spam\eggs') refers to two separate folders (or a file eggs in a folder spam) on Windows, the same command would refer to a single folder (or file) named spam\eggs on macOS and Linux. For this reason, it’s usually a good idea to always use forward slashes in your Python code (and I’ll be doing so for the rest of this chapter). The pathlib module will ensure that it always works on all operating systems.

### Using the / Operator to Join Paths

The / operator that we normally use for division can also combine Path objects and strings

    >>> from pathlib import Path
    >>> Path('spam') / 'bacon' / 'eggs'
    WindowsPath('spam/bacon/eggs')

### The Current Working Directory

Every program that runs on your computer has a current working directory, or cwd. **Any filenames or paths that do not begin with the root folder are assumed to be under the current working directory.**

You can get the current working directory as a string value with the Path.cwd() function and change it using os.chdir().

    >>> from pathlib import Path
    >>> import os
    >>> Path.cwd()
    WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')'

### Absolute vs. Relative Paths

There are two ways to specify a file path:

An absolute path, which always begins with the root folder
A relative path, which is relative to the program’s current working directory

There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”

![paths](/automate_boring_stuff\images\path_dirctory.jpg)

The .\ at the start of a relative path is optional. For example, **.\spam.txt and spam.txt refer to the same file.**

### Creating New Folders Using the os.makedirs() Function

    >>> import os
    >>> os.makedirs('C:\\delicious\\walnut\\waffles')

This will create not just the C:\delicious folder but also a walnut folder inside C:\delicious and a waffles folder inside C:\delicious\walnut. That is, os.makedirs() will create any necessary intermediate folders in order to ensure that the full path exists.

To make a directory from a Path object, call the mkdir() method. For example, this code will create a spam folder under the home folder on my computer:

    >>> from pathlib import Path
    >>> Path(r'C:\Users\Al\spam').mkdir()

Note that mkdir() can only make one directory at a time; it won’t make several subdirectories at once like os.makedirs().

### Handling Absolute and Relative Paths

The os.path module also has some useful functions related to absolute and relative paths:

* Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
* Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
* Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

### Getting the Parts of a File Path

Given a Path object, you can extract the file path’s different parts as strings using several Path object attributes. These can be useful for constructing new file paths based on existing ones. 

The parts of a file path include the following:

* The anchor, which is the root folder of the filesystem
* On Windows, the drive, which is the single letter that often denotes a physical hard drive or other storage device
* The parent, which is the folder that contains the file
* The name of the file, made up of the stem (or base name) and the suffix (or extension)

        >>> p = Path('C:/Users/Al/spam.txt')
        >>> p.anchor
        'C:\\'
        >>> p.parent # This is a Path object, not a string.
        WindowsPath('C:/Users/Al')
        >>> p.name
        'spam.txt'
        >>> p.stem
        'spam'
        >>> p.suffix
        '.txt'
        >>> p.drive
        'C:'

The parents attribute (which is different from the parent attribute) evaluates to the ancestor folders of a Path object with an integer index:

    >>> Path.cwd()
    WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
    >>> Path.cwd().parents[0]
    WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
    >>> Path.cwd().parents[1]
    WindowsPath('C:/Users/Al/AppData/Local/Programs')

The split() string method will work to return a list of each part of the path.

    >>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
    >>> os.path.split(calcFilePath)
    ('C:\\Windows\\System32', 'calc.exe')

    >>> '/usr/bin'.split(os. sep)
    ['', 'usr', 'bin']

### Finding File Sizes and Folder Contents


* Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
* Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)

        >>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
        27648
        >>> os.listdir('C:\\Windows\\System32')
        ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll']

### Modifying a List of Files Using Glob Patterns

Like with regexes, you can create complex expressions:

    >>> list(p.glob('*.txt') # Lists all text files.
    [WindowsPath('C:/Users/Al/Desktop/foo.txt'),
    --snip--
    WindowsPath('C:/Users/Al/Desktop/zzz.txt')]

The glob pattern '*.txt' will return files that start with any combination of characters as long as it ends with the string '.txt', which is the text file extension.

### Checking Path Validity

* Caling p.exists() returns True if the path exists or returns False if it doesn’t exist.
* Calling p.is_file() returns True if the path exists and is a file, or returns False otherwise.
* Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.

### The File Reading/Writing Process

There are three steps to reading or writing files in Python:

* Call the open() function to return a File object.
* Call the read() or write() method on the File object.
* Close the file by calling the close() method on the File object.

#### Opening Files with the open() Function

    >>> helloFile = open(Path.home() / 'hello.txt')

These commands will open the file in “reading plaintext” mode, or read mode for short. When a file is opened in read mode, Python lets you only read data from the file; you can’t write or modify it in any way. Read mode is the default mode for files you open in Python.

### Reading the Contents of Files

If you think of the contents of a file as a single large string value, the read() method returns the string that is stored in the file.

Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text.

### Saving Variables with the shelve Module

Your program can restore data to variables from the hard drive. The shelve module will let you add Save and Open features to your program. For example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load them the next time it is run.

### Saving Variables with the pprint.pformat() Function

pprint.pprint() function will “pretty print” the contents of a list or dictionary to the screen, while the pprint.pformat() function will return this same text as a string instead of printing it. Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use. Using pprint.pformat() will give you a string that you can write to a .py file. This file will be your very own module that you can import whenever you want to use the variable stored in it.

