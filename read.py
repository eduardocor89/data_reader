import csv
import csv


with open('read.csv', 'r') as file: 
    csv_reader = csv.DictReader(file)
    data = []

    for row in csv_reader:
        data.append(row)
    for item in range(len(data)):
        date = data[item]['Date']
        property_name = data[item]['Property Name']
        visit = property_name + ' ' + date
        # print(data[item]['Date'])
        print(visit)

  
    # date = data[0]['Date'] 
    # name = data[0]['Property Name']
    # visit = name + ' ' + date


