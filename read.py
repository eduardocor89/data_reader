import csv
import csv
import matplotlib.pyplot as plt
from collections import Counter

with open('read.csv', 'r') as file: 
    csv_reader = csv.DictReader(file)
    data = []
    same_property_visit = {}


    # read each line and pull from it the property name and date
    # of your visit
    def property_visit():
        for row in csv_reader:
            data.append(row)
        for item in range(len(data)):
            date = data[item]['Date']
            property_name = data[item]['Property Name']
            visit = property_name + ' ' + date
            print(visit)
        return 
    #property_visit()

    def follow_up():
        # Read each line and look for the word 'follow'
        # if it's present, tell me to follow up, which property
        # to follow up and when I was there last.

        for row in csv_reader:
            data.append(row)
        for item in range(len(data)):
            date = data[item]['Date']
            property_name = data[item]['Property Name']
            visit = property_name + ' ' + date
        # Read each row and find the word 'follow' 
            if 'follow' in data[item]['Comments']:
                print("You should follow up on: " + property_name)
                print("Your last visit was on: " + date)
        return
    #follow_up()

    def how_many_times_i_visited_this_property():
        # I want to count the number of times I visited
        # the same property
        for row in csv_reader:
            data.append(row)
        for item in range(len(data)):
            property_name = data[item]['Property Name']
            counter = 1
            if property_name not in same_property_visit:
                same_property_visit[property_name] = counter
            else:
                same_property_visit[property_name] += counter
            # print the list in order of most visited to least
        print(Counter(same_property_visit))
        return
    #how_many_times_i_visited_this_property()

    # Data Visualization
    def plot_dictionary_bar(same_property_visit):
        def how_many_times_i_visited_this_property():
        # I want to count the number of times I visited
        # the same property
            for row in csv_reader:
                data.append(row)
            for item in range(len(data)):
                property_name = data[item]['Property Name']
                counter = 1
                if property_name not in same_property_visit:
                    same_property_visit[property_name] = counter
                else:
                    same_property_visit[property_name] += counter
                # print the list in order of most visited to least
            print(Counter(same_property_visit))
            return
        how_many_times_i_visited_this_property()
        
        keys = same_property_visit.keys()
        values = same_property_visit.values()

        plt.bar(keys,values)
        plt.xlabel('Property Name')
        plt.ylabel('Number of visits')
        plt.title('Property Visits')
        plt.show()
        return
    #plot_dictionary_bar(same_property_visit)

    # NEXT: count how many visits I had every day and draw them on a line graph