## The time Module

Your computer’s system clock is set to a specific date, time, and time zone. The built-in time module allows your Python programs to read the system clock for the current time. The time.time() and time.sleep() functions are the most useful in the time module.

Another way to profile your code is to use the cProfile.run() function, which provides a much more informative level of detail than the simple time.time() technique. The cProfile.run() function is explained at https://docs.python.org/3/library/profile.html.

## Rounding Numbers

When working with times, you’ll often encounter float values with many digits after the decimal. To make these values easier to work with, you can shorten them with Python’s built-in round() function, which rounds a float to the precision you specify. Just pass in the number you want to round, plus an optional second argument representing how many digits after the decimal point you want to round it to. If you omit the second argument, round() rounds your number to the nearest whole integer. Enter the following into the interactive shell:

    >>> import time
    >>> now = time.time()
    >>> now
    1543814036.6147408
    >>> round(now, 2)
    1543814036.61
    >>> round(now, 4)
    1543814036.6147
    >>> round(now)
    1543814037

## The datetime Module

The time module is useful for getting a Unix epoch timestamp to work with. But if you want to display a date in a more convenient format, or do arithmetic with dates (for example, figuring out what date was 205 days ago or what date is 123 days from now), you should use the datetime module.

## The timedelta Data Type

The datetime module also provides a timedelta data type, which represents a duration of time rather than a moment in time. Enter the following into the interactive shell:

    ➊ >>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
    ➋ >>> delta.days, delta.seconds, delta.microseconds
    (11, 36548, 0)
    >>> delta.total_seconds()
    986948.0
    >>> str(delta)
    '11 days, 10:09:08'

There is no month or year keyword argument, because “a month” or “a year” is a variable amount of time depending on the particular month or year.

The arithmetic operators can be used to perform date arithmetic on datetime values.

    >>> dt = datetime.datetime.now()
    >>> dt
    datetime.datetime(2018, 12, 2, 18, 38, 50, 636181)
    >>> thousandDays = datetime.timedelta(days=1000)
    >>> dt + thousandDays
    datetime.datetime(2021, 8, 28, 18, 38, 50, 636181)

timedelta objects can be added or subtracted with datetime objects or other timedelta objects using the + and - operators. A timedelta object can be multiplied or divided by integer or float values with the * and / operators.

## Pausing Until a Specific Date

    import datetime
    import time
    halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
    while datetime.datetime.now() < halloween2016:
        time.sleep(1)

## Converting datetime Objects into Strings

Epoch timestamps and datetime objects aren’t very friendly to the human eye. Use the strftime() method to display a datetime object as a string.

![datetime_visual](/automate_boring_stuff\images\datetime_strftime.png)

    >>> oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
    >>> oct21st.strftime('%Y/%m/%d %H:%M:%S')
    '2019/10/21 16:29:00'
    >>> oct21st.strftime('%I:%M %p')
    '04:29 PM'
    >>> oct21st.strftime("%B of '%y")
    "October of '19"

## Converting Strings into datetime Objects

If you have a string of date information, such as '2019/10/21 16:29:00' or 'October 21, 2019', and need to convert it to a datetime object, use the datetime.datetime.strptime() function.

    ➊ >>> datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
    datetime.datetime(2019, 10, 21, 0, 0)
    >>> datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
    datetime.datetime(2019, 10, 21, 16, 29)
    >>> datetime.datetime.strptime("October of '19", "%B of '%y")
    datetime.datetime(2019, 10, 1, 0, 0)
    >>> datetime.datetime.strptime("November of '63", "%B of '%y")
    datetime.datetime(2063, 11, 1, 0, 0)

## Review of Python’s Time Functions

Dates and times in Python can involve quite a few different data types and functions. Here’s a review of the three different types of values used to represent time:

A Unix epoch timestamp (used by the time module) is a float or integer value of the number of seconds since 12 AM on January 1, 1970, UTC.
A datetime object (of the datetime module) has integers stored in the attributes year, month, day, hour, minute, and second.
A timedelta object (of the datetime module) represents a time duration, rather than a specific moment.
Here’s a review of time functions and their parameters and return values:

* time.time() This function returns an epoch timestamp float value of the current moment.
* time.sleep(seconds) This function stops the program for the number of seconds specified by the seconds argument.
* datetime.datetime(year, month, day, hour, minute, second) This function returns a datetime object of the moment specified by the arguments. If hour, minute, or second arguments are not provided, they default to 0.
* datetime.datetime.now() This function returns a datetime object of the current moment.
* datetime.datetime.fromtimestamp(epoch) This function returns a datetime object of the moment represented by the epoch timestamp argument.
* datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds) This function returns a timedelta object representing a duration of time. The function’s keyword arguments are all optional and do not include month or year.
* total_seconds() This method for timedelta objects returns the number of seconds the timedelta object represents.
* strftime(format) This method returns a string of the time represented by the datetime object in a custom format that’s based on the format string. See Table 17-1 for the format details.
* datetime.datetime.strptime(time_string, format) This function returns a datetime object of the moment specified by time_string, parsed using the format string argument. See Table 17-1 for the format details.

## Multithreading

To introduce the concept of multithreading, let’s look at an example situation. Say you want to schedule some code to run after a delay or at a specific time. You could add code like the following at the start of your program:

    import time, datetime

    startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
    while datetime.datetime.now() < startTime:
        time.sleep(1)

Your program cannot do anything while waiting for the loop of time.sleep() calls to finish; it just sits around until Halloween 2029. This is because Python programs by default have a single thread of execution.

To make a separate thread, you first need to make a Thread object by calling the threading.Thread() function

### Passing Arguments to the Thread’s Target Function

If the target function you want to run in the new thread takes arguments, you can pass the target function’s arguments to threading.Thread().

    >>> import threading
    >>> threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
    kwargs={'sep': ' & '})
    >>> threadObj.start()
    Cats & Dogs & Frogs

## Concurrency Issues

You can easily create several new threads and have them all running at the same time. But multiple threads can also cause problems called concurrency issues. These issues happen when threads read and write variables at the same time, causing the threads to trip over each other.

## Launching Other Programs from Python

Your Python program can start other programs on your computer with the Popen() function in the built-in subprocess module. (The P in the name of the Popen() function stands for process.) If you have multiple instances of an application open, each of those instances is a separate process of the same program. For example, if you open multiple windows of your web browser at the same time, each of those windows is a different process of the web browser program.

If you want to start an external program from your Python script, pass the program’s filename to subprocess.Popen(). (On Windows, right-click the application’s Start menu item and select Properties to view the application’s filename.

The return value is a Popen object, which has two useful methods: poll() and wait().

You can think of the poll() method as asking your driver “Are we there yet?” over and over until you arrive. The poll() method will return None if the process is still running at the time poll() is called. If the program has terminated, it will return the process’s integer exit code. An exit code is used to indicate whether the process terminated without errors (an exit code of 0) or whether an error caused the process to terminate (a nonzero exit code—generally 1, but it may vary depending on the program).

The wait() method is like waiting until the driver has arrived at your destination. The wait() method will block until the launched process has terminated. This is helpful if you want your program to pause until the user finishes with the other program. The return value of wait() is the process’s integer exit code.

## Passing Command Line Arguments to the Popen() Function

You can pass command line arguments to processes you create with Popen(). To do so, you pass a list as the sole argument to Popen(). The first string in this list will be the executable filename of the program you want to launch; all the subsequent strings will be the command line arguments to pass to the program when it starts. In effect, this list will be the value of sys.argv for the launched program.

## Task Scheduler, launchd, and cron

If you are computer savvy, you may know about Task Scheduler on Windows, launchd on macOS, or the cron scheduler on Linux. These well-documented and reliable tools all allow you to schedule applications to launch at specific times.

## Running Other Python Scripts

You can launch a Python script from Python just like any other application. Simply pass the python.exe executable to Popen() and the filename of the .py script you want to run as its argument. 

    >>> subprocess.Popen(['C:\\Users\\<YOUR USERNAME>\\AppData\\Local\\Programs\\
    Python\\Python38\\python.exe', 'hello.py'])

If the script you’re launching needs command line arguments, add them to the list after the script’s filename.

## Opening Files with Default Applications

Double-clicking a .txt file on your computer will automatically launch the application associated with the .txt file extension. Your computer will have several of these file extension associations set up already. Python can also open files this way with Popen().

    >>> fileObj = open('hello.txt', 'w')
    >>> fileObj.write('Hello, world!')
    12
    >>> fileObj.close()
    >>> import subprocess
    >>> subprocess.Popen(['start', 'hello.txt'], shell=True)

Here we write Hello, world! to a new hello.txt file. Then we call Popen(), passing it a list containing the program name (in this example, 'start' for Windows) and the filename. We also pass the shell=True keyword argument, which is needed only on Windows. The operating system knows all of the file associations and can figure out that it should launch, say, Notepad.exe to handle the hello.txt file.

## Summary

Finally, your Python programs can launch other applications with the subprocess.Popen() function. Command line arguments can be passed to the Popen() call to open specific documents with the application. Alternatively, you can use the start, open, or see program with Popen() to use your computer’s file associations to automatically figure out which application to use to open a document. By using the other applications on your computer, your Python programs can leverage their capabilities for your automation needs.

