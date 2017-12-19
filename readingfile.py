import csv


d = {}
d['name'] = []
d['date'] = []

dictReader = csv.DictReader(open('testfile.csv', 'r'), fieldnames = ['name', 'date'], delimiter = ',', quotechar = '"')

for row in dictReader:
    for key in row:
            d[key].append(row[key])

print(d)

# dictReader.close()
