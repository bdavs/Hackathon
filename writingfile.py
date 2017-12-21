import csv
import os.path

def writeToFile(Dict):

#needsHeader = True
#if os.path.exists('testfile.csv'):
#    needsHeader = False

#connect with interface
with open('testfile.csv', 'a') as csvfile:
    fieldnames = ['name', 'date', 'speaker']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i in range(len(Dict['name']))
        name=Dict['name'][i]
        date=Dict['date'][i]
        speaker=Dict['speaker'][i]
        writer.writerow({'name': name, 'date': date, 'speaker':speaker})
	#add remaining field
csvfile.close()
