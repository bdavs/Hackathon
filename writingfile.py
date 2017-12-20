import csv
import os.path

#needsHeader = True
#if os.path.exists('testfile.csv'):
#    needsHeader = False

#connect with interface
with open('testfile.csv', 'a') as csvfile:
    fieldnames = ['name', 'date', 'speaker']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    name = input('Event Name: ' )
    date = input('Event Date: ' )
    speaker = input('Event Speaker: ' )
    writer.writerow({'name': name, 'date': date, 'speaker':speaker})
	#add remaining field
csvfile.close()
