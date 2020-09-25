##Setting Up Your GUI Automation Scripts

GUI automation scripts are a great way to automate the boring stuff, but your scripts can also be finicky. If a window is in the wrong place on a desktop or some pop-up appears unexpectedly, your script could be clicking on the wrong things on the screen. Here are some tips for setting up your GUI automation scripts:

Use the same screen resolution each time you run the script so that the position of windows doesn’t change.
The application window that your script clicks should be maximized so that its buttons and menus are in the same place each time you run the script.
Add generous pauses while waiting for content to load; you don’t want your script to begin clicking before the application is ready.
Use locateOnScreen() to find buttons and menus to click, rather than relying on XY coordinates. If your script can’t find the thing it needs to click, stop the program rather than let it continue blindly clicking.
Use getWindowsWithTitle() to ensure that the application window you think your script is clicking on exists, and use the activate() method to put that window in the foreground.
Use the logging module from Chapter 11 to keep a log file of what your script has done. This way, if you have to stop your script halfway through a process, you can change it to pick up from where it left off.
Add as many checks as you can to your script. Think about how it could fail if an unexpected pop-up window appears or if your computer loses its internet connection.
You may want to supervise the script when it first begins to ensure that it’s working correctly.
You might also want to put a pause at the start of your script so the user can set up the window the script will click on. PyAutoGUI has a sleep() function that acts identically to time.sleep() (it just frees you from having to also add import time to your scripts). There is also a countdown() function that prints numbers counting down to give the user a visual indication that the script will continue soon. Enter the following into the interactive shell:

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

