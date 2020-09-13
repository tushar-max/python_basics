### The shutil Module

The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs. To use the shutil functions, you will first need to use import shutil.

Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination. (Both source and destination can be strings or Path objects.) If destination is a filename, it will be used as the new name of the copied file. This function returns a string or Path object of the copied file.

While shutil.copy() will copy a single file, shutil.copytree() will copy an entire folder and every folder and file contained in it. 

### Moving and Renaming Files and Folders

Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.

If there had been a bacon.txt file already in C:\eggs, it would have been overwritten.

    >>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
    'C:\\eggs\\new_bacon.txt'

This line says, “Move C:\bacon.txt into the folder C:\eggs, and while you’re at it, rename that bacon.txt file to new_bacon.txt.”

Here, move() can’t find a folder named eggs in the C:\ directory and so assumes that destination must be specifying a filename, not a folder. So the bacon.txt text file is renamed to eggs (a text file without the .txt file extension)—probably not what you wanted! This can be a tough-to-spot bug in your programs since the move() call can happily do something that might be quite different from what you were expecting. This is yet another reason to be careful when using move().

### Permanently Deleting Files and Folders

You can delete a single file or a single empty folder with functions in the os module, whereas to delete a folder and all of its contents, you use the shutil module.

* Calling os.unlink(path) will delete the file at path.
* Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
* Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

### Safe Deletes with the send2trash Module

Since Python’s built-in shutil.rmtree() function irreversibly deletes files and folders, it can be dangerous to use. A much better way to delete files and folders is with the third-party send2trash module. You can install this module by running **pip install --user send2trash** from a Terminal window.

    >>> import send2trash
    >>> baconFile = open('bacon.txt', 'a')   # creates the file
    >>> baconFile.write('Bacon is not a vegetable.')
    25
    >>> baconFile.close()
    >>> send2trash.send2trash('bacon.txt')

In general, you should always use the send2trash.send2trash() function to delete files and folders. But while sending files to the recycle bin lets you recover them later, it will not free up disk space like permanently deleting them does.

### Walking a direcotry tree

Here is an example program that uses the os.walk() function on the directory tree from Figure 10-1:

    import os

    for folderName, subfolders, filenames in os.walk('C:\\delicious'):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)

        print('')


### Compressing Files with the zipfile Module

Your Python programs can create and open (or extract) ZIP files using functions in the zipfile module.

### Reading ZIP Files

To read the contents of a ZIP file, first you must create a ZipFile object (note the capital letters Z and F). 

To create a ZipFile object, call the zipfile.ZipFile() function, passing it a string of the .ZIP file’s filename. Note that zipfile is the name of the Python module, and ZipFile() is the name of the function.

### Extracting from ZIP Files

The extractall() method for ZipFile objects extracts all the files and folders from a ZIP file into the current working directory.

    >>> exampleZip.extract('spam.txt')
    'C:\\spam.txt'
    >>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
    'C:\\some\\new\\folders\\spam.txt'

### Creating and Adding to ZIP Files

To create your own compressed ZIP files, you must open the ZipFile object in write mode by passing 'w' as the second argument. 

    >>> import zipfile
    >>> newZip = zipfile.ZipFile('new.zip', 'w')
    >>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    >>> newZip.close()

