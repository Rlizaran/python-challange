import os
import csv

# main function

# This path goes to the directory Resources and select the budget_data.csv file
filepath = os.path.join('Resources', 'election_data.csv')
with open(filepath, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
<<<<<<< HEAD
        for row in csv_reader:
            print(row)


print('Heelo')
=======
        
>>>>>>> b430ac8419b716927f154229d1a7c4eff848b0f3
