In this chapter, you will learn about several modules that make it easy to scrape web pages in Python.

* webbrowser Comes with Python and opens a browser to a specific page.
* requests Downloads files and web pages from the internet.
* bs4 Parses HTML, the format that web pages are written in.
* selenium Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.

## Downloading Files from the Web with the requests Module

The requests module doesn’t come with Python, so you’ll have to install it first. From the command line, run pip install requests.

You can find a complete list of HTTP status codes and their meanings at https://en.wikipedia.org/wiki/List_of_HTTP_status_codes.

## Checking for Errors

As you’ve seen, the Response object has a status_code attribute that can be checked against requests.codes.ok (a variable that has the integer value 200) to see whether the download succeeded. A simpler way to check for success is to call the raise_for_status() method on the Response object.

    >>> res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    >>> res.raise_for_status()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>

If a failed download isn’t a deal breaker for your program, you can wrap the raise_for_status() line with try and except statements to handle this error case without crashing.

    import requests
    res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

Always call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.

## Saving Downloaded Files to the Hard Drive

First, you must open the file in write binary mode by passing the string 'wb' as the second argument to open(). Even if the page is in plaintext (such as the Romeo and Juliet text you downloaded earlier), you need to write binary data instead of text data in order to maintain the Unicode encoding of the text.

    iter_content(chunk_size=1, decode_unicode=False)

Iterates over the response data. When stream=True is set on the request, this avoids reading the content at once into memory for large responses. The chunk size is the number of bytes it should read into memory. This is not necessarily the length of each item returned as decoding can take place.

The iter_content() method returns “chunks” of the content on each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so pass 100000 as the argument to iter_content().


### UNICODE ENCODINGS

Unicode encodings are beyond the scope of this book, but you can learn more about them from these web pages:

Joel on Software: The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!): https://www.joelonsoftware.com/articles/Unicode.html
Pragmatic Unicode: https://nedbatchelder.com/text/unipain.html

## Requests() summary

To review, here’s the complete process for downloading and saving a file:

* Call requests.get() to download the file.
* Call open() with 'wb' to create a new file in write binary mode.
* Loop over the Response object’s iter_content() method.
* Call write() on each iteration to write the content to the file.
* Call close() to close the file.

## Parsing HTML with the bs4 Module

Beautiful Soup is a module for extracting information from an HTML page (and is much better for this purpose than regular expressions). The Beautiful Soup module’s name is bs4 (for Beautiful Soup, version 4). To install it, you will need to run pip install --user beautifulsoup4 from the command line.

## Finding an Element with the select() Method

You can retrieve a web page element from a BeautifulSoup object by calling the select()method and passing a string of a CSS selector for the element you are looking for. Selectors are like regular expressions: they specify a pattern to look for—in this case, in HTML pages instead of general text strings.

The various selector patterns can be combined to make sophisticated matches. For example, soup.select('p #author') will match any element that has an id attribute of author, as long as it is also inside a <p> element. 

Instead of writing the selector yourself, you can also right-click on the element in your browser and select Inspect Element. When the browser’s developer console opens, right-click on the element’s HTML and select Copy ▸ CSS Selector to copy the selector string to the clipboard and paste it into your source code.

## Getting Data from an Element’s Attributes

The get() method for Tag objects makes it simple to access attribute values from an element. The method is passed a string of an attribute name and returns that attribute’s value. 