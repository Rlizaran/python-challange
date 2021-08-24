import os
import csv

# main function
def main():
    # This path goes to the directory Resources and select the budget_data.csv file
    filepath = os.path.join('Resources', 'election_data.csv')
    totalVotes = []
    candidates = []
    votes = [0, 0, 0, 0]
    # Opens csv file as read mode
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')

        # This skips the firts row of the CSV file
        next(csv_reader)
        # Append total amount fo votes to totalVotes and if the candidate is not in candidates list
        # append it as well.
        for row in csv_reader:
            totalVotes.append(row[2])
            if row[2] not in candidates:
                candidates.append(row[2])

    # Calculate total votes for each candidate
    for person in totalVotes:
        if person == candidates[0]:
            votes[0] += 1
        elif person == candidates[1]:
            votes[1] += 1
        elif person == candidates[2]:
            votes[2] += 1
        elif person == candidates[3]:
            votes[3] += 1

    # Calculate percents of votes won for each candidates
    firstCandidate = (votes[0]/len(totalVotes))*100
    secondCandidate = (votes[1]/len(totalVotes))*100
    thirdCandidate = (votes[2]/len(totalVotes))*100
    fourthCandidate = (votes[3]/len(totalVotes))*100

    # Find candidate winner
    winnercandidate = candidates[votes.index(max(votes))]

    # Create variable to hold values to be printed into terminal and text document
    toprint = ("Election Results\n-------------------------\n"
    f"Total Votes: {len(totalVotes)}\n-------------------------\n"
        f"{candidates[0]}: {firstCandidate:9.3f}% ({votes[0]})\n"
        f"{candidates[1]}: {secondCandidate:7.3f}% ({votes[1]})\n"
        f"{candidates[2]}: {thirdCandidate:11.3f}% ({votes[2]})\n"
        f"{candidates[3]}: {fourthCandidate:1.3f}% ({votes[3]})\n"
        f"-------------------------\nWinner: {winnercandidate}\n"
        "-------------------------")
        
    # Print to terminal
    print(toprint)

    # Open path to text file in which the values will be recorded and write those values
    output = os.path.join('analysis','analysis.txt')
    with open (output,'w') as text:
        text.write(toprint)

# Run main function
if __name__ == "__main__":
    main()
