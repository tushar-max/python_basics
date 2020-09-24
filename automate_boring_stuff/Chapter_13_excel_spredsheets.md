Excel is a popular and powerful spreadsheet application for Windows. The openpyxl module allows your Python programs to read and modify Excel spreadsheet files. 

## Installing the openpyxl Module

Python does not come with OpenPyXL, so you’ll have to install it.

This book uses version 2.6.2 of OpenPyXL. It’s important that you install this version by running pip install --user -U openpyxl==2.6.2 because newer versions of OpenPyXL are incompatible with the information in this book.

## Getting Cells from the Sheets

The openpyxl.load_workbook() function takes in the filename and returns a value of the workbook data type. This Workbook object represents the Excel file, a bit like how a File object represents an opened text file.

Remember that example.xlsx needs to be in the current working directory in order for you to work with it. 

Specifying a column by letter can be tricky to program, especially because after column Z, the columns start by using two letters: AA, AB, AC, and so on. As an alternative, you can also get a cell using the sheet’s cell() method and passing integers for its row and column keyword arguments. The first row or column integer is 1, not 0.

## Converting Between Column Letters and Numbers

To convert from letters to numbers, call the openpyxl.utils.column_index_from_string() function. To convert from numbers to letters, call the openpyxl.utils.get_column_letter() function. Enter the following into the interactive shell:

    >>> import openpyxl
    >>> from openpyxl.utils import get_column_letter, column_index_from_string
    >>> get_column_letter(1) # Translate column 1 to a letter.
    'A'
    >>> get_column_letter(2)
    'B'
    >>> get_column_letter(27)
    'AA'
    >>> get_column_letter(900)
    'AHP'

## Getting Rows and Columns from the Sheets

You can slice Worksheet objects to get all the Cell objects in a row, column, or rectangular area of the spreadsheet. 

    >>> import openpyxl
    >>> wb = openpyxl.load_workbook('example.xlsx')
    >>> sheet = wb['Sheet1']
    >>> tuple(sheet['A1':'C3']) # Get all cells from A1 to C3.
    ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell
    'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>,
    <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
    ➊ >>> for rowOfCellObjects in sheet['A1':'C3']:
    ➋ ...     for cellObj in rowOfCellObjects:
    ...         print(cellObj.coordinate, cellObj.value)
    ...     print('--- END OF ROW ---')

This tuple contains three tuples: one for each row, from the top of the desired area to the bottom. Each of these three inner tuples contains the Cell objects in one row of our desired area, from the leftmost cell to the right. So overall, our slice of the sheet contains all the Cell objects in the area from A1 to C3, starting from the top-left cell and ending with the bottom-right cell.

To print the values of each cell in the area, we use two for loops. The outer for loop goes over each row in the slice ➊. Then, for each row, the nested for loop goes through each cell in that row ➋.

## Workbooks, Sheets, Cells

As a quick review, here’s a rundown of all the functions, methods, and data types involved in reading a cell out of a spreadsheet file:

Import the openpyxl module.
Call the openpyxl.load_workbook() function.
Get a Workbook object.
Use the active or sheetnames attributes.
Get a Worksheet object.
Use indexing or the cell() sheet method with row and column keyword arguments.
Get a Cell object.
Read the Cell object’s value attribute.

## Creating and Saving Excel Documents

    >>> import openpyxl
    >>> wb = openpyxl.Workbook() # Create a blank workbook.
    >>> wb.sheetnames # It starts with one sheet.
    ['Sheet']
    >>> sheet = wb.active
    >>> sheet.title
    'Sheet'
    >>> sheet.title = 'Spam Bacon Eggs Sheet' # Change title.
    >>> wb.sheetnames
    ['Spam Bacon Eggs Sheet']

Any time you modify the Workbook object or its sheets and cells, the spreadsheet file will not be saved until you call the save() workbook method.

    >>> wb.save('example_copy.xlsx') # Save the workbook.

Whenever you edit a spreadsheet you’ve loaded from a file, you should always save the new, edited spreadsheet to a different filename than the original. That way, you’ll still have the original spreadsheet file to work with in case a bug in your code caused the new, saved file to have incorrect or corrupt data.

## Formulas
Excel formulas, which begin with an equal sign, can configure cells to contain values calculated from other cells. In this section, you’ll use the openpyxl module to programmatically add formulas to cells, just like any normal value. For example:

    >>> sheet['B9'] = '=SUM(B1:B8)'

This will store =SUM(B1:B8) as the value in cell B9. This sets the B9 cell to a formula that calculates the sum of values in cells B1 to B8.

