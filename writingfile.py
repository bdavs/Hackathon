import csv

with open('testfile.csv', 'w') as csvfile:
    fieldnames = ['name', 'date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'Bobby', 'date': 'Beans'})
csvfile.close()
