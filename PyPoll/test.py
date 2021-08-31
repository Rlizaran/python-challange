import os
import csv

# main function

# This path goes to the directory Resources and select the budget_data.csv file
filepath = os.path.join('Resources', 'election_data.csv')
with open(filepath, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            print(row)


print('Heelo')