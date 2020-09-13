import shutil, os
from pathlib import Path

p = Path.home()

shutil.copy(p / "hello.txt", p / "same_folder")

shutil.copy(p / "hello.txt", p / "same_folder/eggs2.txt")

# 1. the original spam.txt filename is used for the new, copied file’s filename. The second shutil.copy() call
# 2. also copies the file at C:\Users\Al\eggs.txt to the folder C:\Users\Al\some_folder but gives the copied file the name eggs2.txt.

# Zip files

import zipfile

p = Path.home()

exampleZip = zipfile.ZipFile(p / "example.zip")

print(exampleZip.namelist())

zhopie = exampleZip.getinfo("example/zhopie.txt")
print(zhopie.file_size)
print(zhopie.compress_size)


exampleZip.close()

# Extracting

exampleZip  = zipfile.ZipFile(p / "example.zip")
# current directory is where the file of this code are.
exampleZip.extractall()

exampleZip.close()