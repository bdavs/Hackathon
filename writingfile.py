import csv

#connect with interface
with open('testfile.csv', 'w') as csvfile:
    fieldnames = ['name', 'date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    name = input('Event Name: ' )
    date = input('Event Date: ' )
    writer.writerow({'name': name, 'date': date})
	#add remaining fields
csvfile.close()
