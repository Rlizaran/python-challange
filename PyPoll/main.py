import os
import csv

def main():
    # This path goes to the directory Resources and select the budget_data.csv file
    filepath = os.path.join('Resources','election_data.csv')
    totalVotes = []
    candidates = []
    votes = [0,0,0,0]
    #Opens csv file as read mode
    with open(filepath,'r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        # This skips the firts row of the CSV file
        next(csv_reader)
        # Append months to month list and profit/losses to profit_losses list
        for row in csv_reader:
            totalVotes.append(row[2])
            if row[2] not in candidates:
                candidates.append(row[2])
        
        for person in totalVotes:
            if person == candidates[0]:
                votes[0]+=1
            elif person == candidates[1]:
                votes[1]+=1
            elif person ==candidates[2]:
                votes[2]+=1
            elif person == candidates[3]:
                votes[3]+=1
        
        #Calculate percents
        firstCandidate = (votes[0]/len(totalVotes))*100
        secondCandidate = (votes[1]/len(totalVotes))*100
        thirdCandidate = (votes[2]/len(totalVotes))*100
        fourthCandidate = (votes[3]/len(totalVotes))*100
        
        #Calculate winner
        winner = []
        winner.append(firstCandidate,secondCandidate,thirdCandidate,fourthCandidate)
        winnercandidate = max(winner)

        print (f'{candidates[0]}: {firstCandidate:9.3f}% ({votes[0]})')
        print(f'{candidates[1]}: {secondCandidate:7.3f}% ({votes[1]})')
        print(f'{candidates[2]}: {thirdCandidate:11.3f}% ({votes[2]})')
        print(f'{candidates[3]}: {fourthCandidate:1.3f}% ({votes[3]})')
        print(winnercandidate)
        

            
        

        # toprint = f"Election Results\n-------------------------\nTotal Votes: {len(totalVotes)}\n-------------------------\n"
        # print(toprint)
        

if __name__ == "__main__":
    main()
            