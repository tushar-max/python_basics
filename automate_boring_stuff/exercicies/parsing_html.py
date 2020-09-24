import requests, bs4
"""
This code uses requests.get() to download the main page from the No Starch Press website
and then passes the text attribute of the response to bs4.BeautifulSoup(). 
The BeautifulSoup object that it returns is stored in a variable named noStarchSoup.
res = requests.get("https://nostarch.com")

res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))
"""

"""
load an HTML file from your hard drive by passing a File object to bs4.BeautifulSoup()
"""

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")

print(type(exampleSoup))

elems = exampleSoup.select("#author")

print(type(elems))
print(elems)

print(elems[0].getText())

print(elems[0].attrs)

"""
This time, select() gives us a list of three matches, which we store in pElems.
Using str() on pElems[0], pElems[1], and pElems[2] shows you each element as a string,
and using getText() on each element shows you its text.
"""
pElements = exampleSoup.select("p")
print(str(pElements))
print(pElements[0].getText())
print(pElements[1].getText())
print(pElements[2].getText())

print("--------------------------------")

spanElemnt = exampleSoup.select("span")[0]
print(str(spanElemnt))
spanElemnt.get("id")
