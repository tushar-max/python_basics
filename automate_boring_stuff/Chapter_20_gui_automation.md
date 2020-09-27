You can find the full documentation at https://pyautogui.readthedocs.io/.

## Setting Up Your GUI Automation Scripts

GUI automation scripts are a great way to automate the boring stuff, but your scripts can also be finicky. If a window is in the wrong place on a desktop or some pop-up appears unexpectedly, your script could be clicking on the wrong things on the screen. Here are some tips for setting up your GUI automation scripts:

* Use the same screen resolution each time you run the script so that the position of windows doesn’t change.
* The application window that your script clicks should be maximized so that its buttons and menus are in the same place each time you run the script.
* Add generous pauses while waiting for content to load; you don’t want your script to begin clicking before the application is ready.
* Use locateOnScreen() to find buttons and menus to click, rather than relying on XY coordinates. If your script can’t find the thing it needs to click, stop the program rather than let it continue blindly clicking.
* Use getWindowsWithTitle() to ensure that the application window you think your script is clicking on exists, and use the activate() method to put that window in the foreground.
* Use the logging module from Chapter 11 to keep a log file of what your script has done. This way, if you have to stop your script halfway through a process, you can change it to pick up from where it left off.
* Add as many checks as you can to your script. Think about how it could fail if an unexpected pop-up window appears or if your computer loses its internet connection.
* You may want to supervise the script when it first begins to ensure that it’s working correctly.
* You might also want to put a pause at the start of your script so the user can set up the window the script will click on. PyAutoGUI has a sleep() function that acts identically to time.sleep() (it just frees you from having to also add import time to your scripts). * There is also a countdown() function that prints numbers counting down to give the user a visual indication that the script will continue soon. Enter the following into the interactive shell:

    >>> import pyautogui
    >>> pyautogui.sleep(3) # Pauses the program for 3 seconds.
    >>> pyautogui.countdown(10) # Counts down over 10 seconds.
    10 9 8 7 6 5 4 3 2 1
    >>> print('Starting in ', end=''); pyautogui.countdown(3)
    Starting in 3 2 1

These tips can help make your GUI automation scripts easier to use and more able to recover from unforeseen circumstances.

## Review of the PyAutoGUI Functions

Since this chapter covered many different functions, here is a quick summary reference:

* moveTo(x, y) Moves the mouse cursor to the given x and y coordinates.
* move(xOffset, yOffset) Moves the mouse cursor relative to its current position.
* dragTo(x, y) Moves the mouse cursor while the left button is held down.
* drag(xOffset, yOffset) Moves the mouse cursor relative to its current position while the left button is held down.
* click(x, y, button) Simulates a click (left button by default).
* rightClick() Simulates a right-button click.
* middleClick() Simulates a middle-button click.
* doubleClick() Simulates a double left-button click.
* mouseDown(x, y, button) Simulates pressing down the given button at the position x, y.
* mouseUp(x, y, button) Simulates releasing the given button at the position x, y.
* scroll(units) Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls down.
* write(message) Types the characters in the given message string.
* write([key1, key2, key3]) Types the given keyboard key strings.
* press(key) Presses the given keyboard key string.
* keyDown(key) Simulates pressing down the given keyboard key.
* keyUp(key) Simulates releasing the given keyboard key.
* hotkey([key1, key2, key3]) Simulates pressing the given keyboard key strings down in order and then releasing them in reverse order.
* screenshot() Returns a screenshot as an Image object. (See Chapter 19 for information on Image objects.)
* getActiveWindow(), getAllWindows(), getWindowsAt(), and getWindowsWithTitle() These functions return Window objects that can resize and reposition application windows on the desktop.
* getAllTitles() Returns a list of strings of the title bar text of every window on the desktop.


To install PyAutoGUI, run pip install --user pyautogui.

## Pauses and Fail-Safes

If your program has a bug and you’re unable to use the keyboard and mouse to shut it down, you can use PyAutoGUI’s fail-safe feature. Quickly slide the mouse to one of the four corners of the screen. Every PyAutoGUI function call has a 10th-of-a-second delay after performing its action to give you enough time to move the mouse to a corner. If PyAutoGUI then finds that the mouse cursor is in a corner, it raises the pyautogui.FailSafeException exception.

## Planning Your Mouse Movements

One of the difficulties of writing a program that will automate clicking the screen is finding the x- and y-coordinates of the things you’d like to click. The pyautogui.mouseInfo() function can help you with this.

The pyautogui.mouseInfo() function is meant to be called from the interactive shell, rather than as part of your program. It launches a small application named MouseInfo that’s included with PyAutoGUI. 

## Image Recognition

Remember locateOnScreen() raises an exception if it can’t find the image on the screen, so you should call it from inside a try statement:

    try:
        location = pyautogui.locateOnScreen('submit.png')
    except:
        print('Image could not be found.')

Without the try and except statements, the uncaught exception would crash your program. Since you can’t be sure that your program will always find the image, it’s a good idea to use the try and except statements when calling locateOnScreen().

## Obtaining the Active Window

The active window on your screen is the window currently in the foreground and accepting keyboard input. 
**sera que da para identificar o numero da empresa onde se esta com o fw.title'**

    >>> import pyautogui
    >>> fw = pyautogui.getActiveWindow()
    >>> fw
    Win32Window(hWnd=2034368)
    >>> str(fw)
    '<Win32Window left="500", top="300", width="2070", height="1208", title="Mu 1.0.1 – test1.py">'
    >>> fw.title
    'Mu 1.0.1 – test1.py'
    >>> fw.size
    (2070, 1208)

You can now use these attributes to calculate precise coordinates within a window. If you know that a button you want to click is always 10 pixels to the right of and 20 pixels down from the window’s top-left corner, and the window’s top-left corner is at screen coordinates (300, 500), then calling pyautogui.click(310, 520) (or pyautogui.click(fw.left + 10, fw.top + 20) if fw contains the Window object for the window) will click the button. This way, you won’t have to rely on the slower, less reliable locateOnScreen() function to find the button for you.

The following four functions return a list of Window objects. If they’re unable to find any windows, they return an empty list:

* pyautogui.getAllWindows() Returns a list of Window objects for every visible window on the screen.
* pyautogui.getWindowsAt(x, y) Returns a list of Window objects for every visible window that includes the point (x, y).
* pyautogui.getWindowsWithTitle(title) Returns a list of Window objects for every visible window that includes the string title in its title bar.
* pyautogui.getActiveWindow() Returns the Window object for the window that is currently receiving keyboard focus.
* PyAutoGUI also has a pyautogui.getAllTitles() function, which returns a list of strings of every visible window.

## Controlling the Keyboard

![keys](/automate_boring_stuff\images\key_keybord.png)

pyautogui.hotkey() function, which takes multiple keyboard key string arguments, presses them in order, and releases them in the reverse order. For the CTRL-C example, the code would simply be as follows:

    pyautogui.hotkey('ctrl', 'c')

## Displaying Message Boxes

To solve this, PyAutoGUI offers pop-up message boxes to provide notifications to the user and receive input from them. There are four message box functions:

* pyautogui.alert(text) Displays text and has a single OK button.
* pyautogui.confirm(text) Displays text and has OK and Cancel buttons, returning either 'OK' or 'Cancel' depending on the button clicked.
* pyautogui.prompt(text) Displays text and has a text field for the user to type in, which it returns as a string.
* pyautogui.password(text) Is the same as prompt(), but displays asterisks so the user can enter sensitive information such as a password.

These functions also have an optional second parameter that accepts a string value to use as the title in the title bar of the message box.

    >>> import pyautogui
    >>> pyautogui.alert('This is a message.', 'Important')
    'OK'
    >>> pyautogui.confirm('Do you want to continue?') # Click Cancel
    'Cancel'
    >>> pyautogui.prompt("What is your cat's name?")
    'Zophie'
    >>> pyautogui.password('What is the password?')
    'hunter2'

