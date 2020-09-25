import PyPDF2

# Openning and reading the pdf file
pdfFileObj = open("example_pdf.pdf","rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get the number of pages
print(pdfReader.numPages)

# Get the first page & extract text
pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

# Coping to another pdf file
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    current_page = pdfReader.getPage(pageNum)
    pdfWriter.addPage(current_page)

pdfOutputFile = open("copyied_pdf.pdf", "wb")

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()

# Rotate Pages

pageObj.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageObj)

resultPdfFile = open("rotatePage.pdf", "wb")
pdfWriter.write(resultPdfFile)

resultPdfFile.close()


pdfFileObj.close()