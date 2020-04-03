import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData


#Loop
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
