import os
import csv

def main():
    # This path goes to the directory Resources and select the budget_data.csv file
    filepath = os.path.join('Resources','budget_data.csv')
    month = []
    profit_losses = []
    monthlyProfitChange = []

    #Opens csv file as read mode
    with open(filepath,'r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        # This skips the firts row of the CSV file
        next(csv_reader)
        # Append months to month list and profit/losses to profit_losses list
        for row in csv_reader:
            month.append(row[0])
            profit_losses.append(int(row[1]))

    # Calculate monthly average change
    for i in range(len(profit_losses)-1):
        # Calculate difference between two months and append it to montlyProfitChange list
        monthlyProfitChange.append(profit_losses[i+1]-profit_losses[i])
    # Find average change and round to 2 decimal places
    averageChange = round(sum(monthlyProfitChange)/len(monthlyProfitChange),2)

    #Obtain max and min in monhtly profit change (only integers)
    MaxIncrease = max(monthlyProfitChange)
    MinIncrease = min(monthlyProfitChange)

    #Add proper month to the max and min profit changes
    MaxIncreaseMonth = monthlyProfitChange.index(max(monthlyProfitChange))+1
    MinIncreaseMonth = monthlyProfitChange.index(min(monthlyProfitChange))+1

    monthmax = month[MaxIncreaseMonth]
    monthmin = month[MinIncreaseMonth]

    #Print values into terminal
    printing(month,profit_losses, averageChange,MaxIncrease,MinIncrease,monthmax,monthmin)

    #Print values into a txt file
    textpath = os.path.join('analysis','Results.txt')
    with open(textpath,'w') as text:
        dollar = "$"
        writing = f"Financial Analysis\n-------------------------------------\nTotal Months: {len(month):28}\n"
        writing1 =f"Total: {dollar:>33}{sum(profit_losses)}\nAverage Change: {dollar:>24}{averageChange}\n"
        writing2= f"Greatest Increase in Profits: {monthmax} ${MaxIncrease}\nGreatest Decrease in Profits: {monthmin} ${MinIncrease}"
        text.write(writing)
        text.write(writing1)
        text.write(writing2)


# Print solutions into the terminal
def printing(month, profit_losses,average_change,MaxIncrease,MinIncrease,monthmax,monthmin):
    dollar = "$"
    print('Financial Analysis\n-------------------------------------')
    # Clean print into terminal
    print(f'Total Months: {len(month):28}\nTotal: {dollar:>33}{sum(profit_losses)}\nAverage Change: {dollar:>24}{average_change}')
    print(f'Greatest Increase in Profits: {monthmax} ${MaxIncrease}')
    print(f'Greatest Decrease in Profits: {monthmin} ${MinIncrease}')

if __name__ == "__main__":
    main()


