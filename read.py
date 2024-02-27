import csv
import csv


with open('read.csv', 'r') as file: 
    csv_reader = csv.DictReader(file)
    data = []
    # read each line and pull from it the property name and date
    # of your visit
    for row in csv_reader:
        data.append(row)
    for item in range(len(data)):
        date = data[item]['Date']
        property_name = data[item]['Property Name']
        visit = property_name + ' ' + date
        #print(visit)

        # Read each row and find the word 'follow' 
        if 'follow' in data[item]['Comments']:
            print("You should follow up on: " + property_name)
            print("Your last visit was on: " + date)

    # I want to count
  
    # date = data[0]['Date'] 
    # name = data[0]['Property Name']
    # visit = name + ' ' + date


