import csv


exampleFile = open("example1.csv")

exampleReader = csv.reader(exampleFile)

#exampleData = list(exampleReader)

#print(exampleData)
# Porque isto é um ficheiro, a medida que vamos lendo vai ser onde vai ficar para uma outra leitura
for row in exampleReader:
    print("Row #" + str(exampleReader.line_num) + " " + str(row))


exampleFile.close()