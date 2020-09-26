CSV stands for “comma-separated values,” and CSV files are simplified spreadsheets stored as plaintext files. Python’s csv module makes it easy to parse CSV files.

JSON is a format that stores information as JavaScript source code in plaintext files. (JSON is short for JavaScript Object Notation.) You don’t need to know the JavaScript programming language to use JSON files, but the JSON format is useful to know because it’s used in many web applications.

CSV files are simple, lacking many of the features of an Excel spreadsheet. For example, CSV files:

* Don’t have types for their values—everything is a string
* Don’t have settings for font size or color
* Don’t have multiple worksheets
* Can’t specify cell widths and heights
* Can’t have merged cells
* Can’t have images or charts embedded in them

## reader Objects

To read data from a CSV file with the csv module, you need to create a reader object. A reader object lets you iterate over lines in the CSV file.

The csv module comes with Python, so we can import it ➊ without having to install it first.

## writer Objects

A writer object lets you write data to a CSV file. To create a writer object, you use the csv.writer() function. Enter the following into the interactive shell:

    >>> import csv
    ➊ >>> outputFile = open('output.csv', 'w', newline='')
    ➋ >>> outputWriter = csv.writer(outputFile)
    >>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
    21
    >>> outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
    32
    >>> outputWriter.writerow([1, 2, 3.141592, 4])
    16
    >>> outputFile.close()

First, call open() and pass it 'w' to open a file in write mode ➊. This will create the object you can then pass to csv.writer() ➋ to create a writer object.

On Windows, you’ll also need to pass a blank string for the open() function’s newline keyword argument. 

## The delimiter and lineterminator Keyword Arguments

Say you want to separate cells with a tab character instead of a comma and you want the rows to be double-spaced. You could enter something like the following into the interactive shell:

    >>> import csv
    >>> csvFile = open('example.tsv', 'w', newline='')
    ➊ >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
    >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
    24
    >>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
    17
    >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
    32
    >>> csvFile.close()

You can change characters to different values by using the delimiter and lineterminator keyword arguments with csv.writer().

Passing delimiter='\t' and lineterminator='\n\n' ➊ changes the character between cells to a tab and the character between rows to two newlines. We then call writerow() three times to give us three rows.

Now that our cells are separated by tabs, we’re using the file extension .tsv, for tab-separated values.

## DictReader and DictWriter CSV Objects

For CSV files that contain header rows, it’s often more convenient to work with the DictReader and DictWriter objects, rather than the reader and writer objects.

The reader and writer objects read and write to CSV file rows by using lists. The DictReader and DictWriter CSV objects perform the same functions but use dictionaries instead, and they use the first row of the CSV file as the keys of these dictionaries.

    >>> import csv
    >>> exampleFile = open('exampleWithHeader.csv')
    >>> exampleDictReader = csv.DictReader(exampleFile)
    >>> for row in exampleDictReader:
    ...     print(row['Timestamp'], row['Fruit'], row['Quantity'])
    ...
    4/5/2015 13:34 Apples 73
    4/5/2015 3:41 Cherries 85
    4/6/2015 12:46 Pears 14
    4/8/2015 8:59 Oranges 52
    4/10/2015 2:07 Apples 152
    4/10/2015 18:10 Bananas 23
    4/10/2015 2:40 Strawberries 98

If you tried to use DictReader objects with example.csv, which doesn’t have column headers in the first row, the DictReader object would use '4/5/2015 13:34', 'Apples', and '73' as the dictionary keys. To avoid this, you can supply the DictReader() function with a second argument containing made-up header names:

    >>> import csv
    >>> exampleFile = open('example.csv')
    >>> exampleDictReader = csv.DictReader(exampleFile, ['time', 'name',
    'amount'])

DictWriter objects use dictionaries to create CSV files.

    >>> import csv
    >>> outputFile = open('output.csv', 'w', newline='')
    >>> outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
    >>> outputDictWriter.writeheader()
    >>> outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-
    1234'})
    20
    >>> outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
    15
    >>> outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':
    'dog'})
    20
    >>> outputFile.close()

If you want your file to contain a header row, write that row by calling writeheader(). Otherwise, skip calling writeheader() to omit a header row from the file.

## JSON and APIs

Using APIs, you could write programs that do the following:

* Scrape raw data from websites. (Accessing APIs is often more convenient than downloading web pages and parsing HTML with Beautiful Soup.)
* Automatically download new posts from one of your social network accounts and post them to another account. For example, you could take your Tumblr posts and post them to Facebook.
* Create a “movie encyclopedia” for your personal movie collection by pulling data from IMDb, Rotten Tomatoes, and Wikipedia and putting it into a single text file on your computer.

## The json Module

Python’s json module handles all the details of translating between a string with JSON data and Python values for the json.loads() and json.dumps() functions. JSON can’t store every kind of Python value. It can contain values of only the following data types: strings, integers, floats, Booleans, lists, dictionaries, and NoneType. JSON cannot represent Python-specific objects, such as File objects, CSV reader or writer objects, Regex objects, or Selenium WebElement objects.
