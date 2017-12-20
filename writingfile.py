import csv
import os.path

#needsHeader = True
#if os.path.exists('testfile.csv'):
#    needsHeader = False

#connect with interface
with open('testfile.csv', 'a') as csvfile:
    fieldnames = ['name', 'date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    name = input('Event Name: ' )
    date = input('Event Date: ' )
    writer.writerow({'name': name, 'date': date})
	#add remaining fields
csvfile.close()
