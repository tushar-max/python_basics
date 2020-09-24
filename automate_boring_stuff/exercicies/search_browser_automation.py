"""
It would be nice if I could simply type a search term on the command line and have my computer automatically
open a browser with all the top search results in new tabs. 

This is what your program does:

Gets search keywords from the command line arguments
Retrieves the search results page
Opens a browser tab for each result
This means your code will need to do the following:

Read the command line arguments from sys.argv.
Fetch the search result page with the requests module.
Find the links to each search result.
Call the webbrowser.open() function to open the web browser.

"""

import requests, sys, webbrowser, bs4

print('Searching...')    # display text while downloading the search result page

res = requests.get('https://google.com/search?q=''https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Now you need to use Beautiful Soup to extract the top search result links from your downloaded HTML.
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# It looks like the package-snippet class is used only for search result links.
linkElems = soup.select('.package-snippet')

# we’ll tell the program to open web browser tabs for our results.
# min() returns the smallest of the integer or float arguments it is passed.
numOpen = min(5, len(linkElems))
# soup.select() call returns a list of all the elements that matched your '.package-snippet' selector, 
# so the number of tabs you want to open is either 5 or the length of this list (whichever is smaller).

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

