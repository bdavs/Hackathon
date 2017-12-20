import csv
import os.path

def fileToDict():
    d = {}
    d['name'] = []
    d['date'] = []
    #add remaining fields
    if not os.path.exists('testfile.csv'):
        return(-1)
    dictReader = csv.DictReader(open('testfile.csv', 'r'), fieldnames = ['name', 'date'], delimiter = ',', quotechar = '"')

    for row in dictReader:
        for key in row:
            d[key].append(row[key])
    return(d)
#return data to interface #done
#e = fileToDict()
#print(e)
