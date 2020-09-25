## PDF Documents

PDF stands for Portable Document Format and uses the .pdf file extension. Although PDFs support many features, this chapter will focus on the two things you’ll be doing most often with them: reading text content from PDFs and crafting new PDFs from existing documents.

The module you’ll use to work with PDFs is PyPDF2 version 1.26.0. It’s important that you install this version because future versions of PyPDF2 may be incompatible with the code. To install it, run pip install --user PyPDF2==1.26.0 from the command line.

## Decrypting PDFs

Some PDF documents have an encryption feature that will keep them from being read until whoever is opening the document provides a password. Enter the following into the interactive shell with the PDF you downloaded, which has been encrypted with the password rosebud:

    >>> import PyPDF2
    >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
    ➊ >>> pdfReader.isEncrypted
    True
    >>> pdfReader.getPage(0)
    ➋ Traceback (most recent call last):
        File "<pyshell#173>", line 1, in <module>
        pdfReader.getPage()
        --snip--
        File "C:\Python34\lib\site-packages\PyPDF2\pdf.py", line 1173, in getObject
        raise utils.PdfReadError("file has not been decrypted")
    PyPDF2.utils.PdfReadError: file has not been decrypted
    >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
    ➌ >>> pdfReader.decrypt('rosebud')
    1
    >>> pageObj = pdfReader.getPage(0)

## Creating PDFs

PyPDF2’s counterpart to PdfFileReader is PdfFileWriter, which can create new PDF files. But PyPDF2 cannot write arbitrary text to a PDF like Python can do with plaintext files. Instead, PyPDF2’s PDF-writing capabilities are limited to copying pages from other PDFs, rotating pages, overlaying pages, and encrypting files.

* Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
* Create a new PdfFileWriter object.
* Copy pages from the PdfFileReader objects into the PdfFileWriter object.
* Finally, use the PdfFileWriter object to write the output PDF.

## Overlaying Pages

PyPDF2 can also overlay the contents of one page over another, which is useful for adding a logo, timestamp, or watermark to a page. With Python, it’s easy to add watermarks to multiple files and only to pages your program specifies.

Download watermark.pdf from https://nostarch.com/automatestuff2/ and place the PDF in the current working directory along with meetingminutes.pdf. Then enter the following into the interactive shell:

   >>> import PyPDF2
   >>> minutesFile = open('meetingminutes.pdf', 'rb')
➊ >>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
➋ >>> minutesFirstPage = pdfReader.getPage(0)
➌ >>> pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
➍ >>> minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
➎ >>> pdfWriter = PyPDF2.PdfFileWriter()
➏ >>> pdfWriter.addPage(minutesFirstPage)

➐ >>> for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)

   >>> resultPdfFile = open('watermarkedCover.pdf', 'wb')
   >>> pdfWriter.write(resultPdfFile)
   >>> minutesFile.close()
   >>> resultPdfFile.close()

## Encrypting PDFs

A PdfFileWriter object can also add encryption to a PDF document. Enter the following into the interactive shell:

   >>> import PyPDF2
   >>> pdfFile = open('meetingminutes.pdf', 'rb')
   >>> pdfReader = PyPDF2.PdfFileReader(pdfFile)
   >>> pdfWriter = PyPDF2.PdfFileWriter()
   >>> for pageNum in range(pdfReader.numPages):
           pdfWriter.addPage(pdfReader.getPage(pageNum))

➊ >>> pdfWriter.encrypt('swordfish')
   >>> resultPdf = open('encryptedminutes.pdf', 'wb')
   >>> pdfWriter.write(resultPdf)
   >>> resultPdf.close()

## Find All PDF Files

First, your program needs to get a list of all files with the .pdf extension in the current working directory and sort them. Make your code look like the following:

   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # into a single PDF.

➊ import PyPDF2, os
   # Get all the PDF filenames.
   pdfFiles = []
   for filename in os.listdir('.'):
       if filename.endswith('.pdf'):
         ➋ pdfFiles.append(filename)
➌ pdfFiles.sort(key = str.lower)

➍ pdfWriter = PyPDF2.PdfFileWriter()


## Word Documents

Python can create and modify Word documents, which have the .docx file extension, with the docx module. You can install the module by running pip install --user -U python-docx==0.8.10.

## Getting the Full Text from a .docx File

If you care only about the text, not the styling information, in the Word document, you can use the getText() function. It accepts a filename of a .docx file and returns a single string value of its text. 

## Run Attributes

Runs can be further styled using text attributes. Each attribute can be set to one of three values: True (the attribute is always enabled, no matter what other styles are applied to the run), False (the attribute is always disabled), or None (defaults to whatever the run’s style is set to).

    >>> import docx
    >>> doc = docx.Document('demo.docx')
    >>> doc.paragraphs[0].text
    'Document Title'
    >>> doc.paragraphs[0].style # The exact id may be different:
    _ParagraphStyle('Title') id: 3095631007984
    >>> doc.paragraphs[0].style = 'Normal'
    >>> doc.paragraphs[1].text
    'A plain paragraph with some bold and some italic'
    >>> (doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.
    paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text)
    ('A plain paragraph with some ', 'bold', ' and some ', 'italic')
    >>> doc.paragraphs[1].runs[0].style = 'QuoteChar'
    >>> doc.paragraphs[1].runs[1].underline = True
    >>> doc.paragraphs[1].runs[3].underline = True
    >>> doc.save('restyled.docx')

## Writing Word Documents

You can add paragraphs by calling the add_paragraph() method again with the new paragraph’s text. Or to add text to the end of an existing paragraph, you can call the paragraph’s add_run() method and pass it a string. Enter the following into the interactive shell:

    >>> import docx
    >>> doc = docx.Document()
    >>> doc.add_paragraph('Hello world!')
    <docx.text.Paragraph object at 0x000000000366AD30>
    >>> paraObj1 = doc.add_paragraph('This is a second paragraph.')
    >>> paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
    >>> paraObj1.add_run(' This text is being added to the second paragraph.')
    <docx.text.Run object at 0x0000000003A2C860>
    >>> doc.save('multipleParagraphs.docx')

## Adding Headings

Calling add_heading() adds a paragraph with one of the heading styles. Enter the following into the interactive shell:

    >>> doc = docx.Document()
    >>> doc.add_heading('Header 0', 0)
    <docx.text.Paragraph object at 0x00000000036CB3C8>
    >>> doc.add_heading('Header 1', 1)
    <docx.text.Paragraph object at 0x00000000036CB630>
    >>> doc.add_heading('Header 2', 2)
    <docx.text.Paragraph object at 0x00000000036CB828>

## Adding Pictures

Document objects have an add_picture() method that will let you add an image to the end of the document. Say you have a file zophie.png in the current working directory. You can add zophie.png to the end of your document with a width of 1 inch and height of 4 centimeters (Word can use both imperial and metric units) by entering the following:

    >>> doc.add_picture('zophie.png', width=docx.shared.Inches(1),
    height=docx.shared.Cm(4))
    <docx.shape.InlineShape object at 0x00000000036C7D30>

The first argument is a string of the image’s filename. The optional width and height keyword arguments will set the width and height of the image in the document. If left out, the width and height will default to the normal size of the image.

## Creating PDFs from Word Documents

The PyPDF2 module doesn’t allow you to create PDF documents directly, but there’s a way to generate PDF files with Python if you’re on Windows and have Microsoft Word installed. You’ll need to install the Pywin32 package by running pip install --user -U pywin32==224. With this and the docx module, you can create Word documents and then convert them to PDFs with the following script.

Open a new file editor tab, enter the following code, and save it as convertWordToPDF.py:

    # This script runs on Windows only, and you must have Word installed.
    import win32com.client # install with "pip install pywin32==224"
    import docx
    wordFilename = 'your_word_document.docx'
    pdfFilename = 'your_pdf_filename.pdf'

    doc = docx.Document()
    # Code to create Word document goes here.
    doc.save(wordFilename)

    wdFormatPDF = 17 # Word's numeric code for PDFs.
    wordObj = win32com.client.Dispatch('Word.Application')

    docObj = wordObj.Documents.Open(wordFilename)
    docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
    docObj.Close()
    wordObj.Quit()
