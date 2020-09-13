from pathlib import Path
import os

Path.home()                
helloFile = open(Path.home()/"hello.txt")

helloContent = helloFile.read()
print(helloContent)

helloFile.close()



helloFile = open(Path.home()/"hello.txt")

helloReaLines = helloFile.readlines()

print(helloReaLines)
# ['Hello World!!\n', '\n', "When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n',
#  'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']

helloFile.close()


path = Path.cwd() / "automate_boring_stuff" / "exercicies" / "bacon.txt"
print(path)
baconFile = open(path, "w")
baconFile.write("Hello, world!\n")
baconFile.close()

baconFile = open(path, "a")
baconFile.write("Bacon is not a vegetable.")
baconFile.close()

baconFile = open(path)
content = baconFile.read()
baconFile.close()

print(content)

# Saving Variables with the Shelve Module - Create

import shelve

path = "./automate_boring_stuff/exercicies/mydata"

shelveFile = shelve.open(path)
cats = ["Zophie","Pooka","Simon"]
# You can make changes to the shelf value as if it were a dictionary.
shelveFile["cats"] = cats
shelveFile.close()

# Read and modified

shelveFile = shelve.open(path)
type(shelveFile)
print(shelveFile["cats"])
shelveFile.close()

# Saving text with pprint.pformat()

import pprint

cats = [{"name":"Zophie", "desc":"chubby"},{"name":"Pooka", "desc": "fluffy"}]

print(cats)
# To keep the list in cats available even after we close the shell, we use pprint.pformat() to return it as a string.
pprint.pformat(cats)

path = Path.cwd() / "automate_boring_stuff" / "exercicies" / "myCats.py"

fileObj = open(path, "w")

fileObj.write("cats = " + pprint.pformat(cats) + "\n")

fileObj.close()