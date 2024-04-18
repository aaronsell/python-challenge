import os
import csv

' set the file path for the csv file '
csvpath = os.path.join("election_data.csv")

' set the output path'
electionText = os.path.join("pyPoll.txt")

' set and initialize variables'
totalVotes = 0
voteSummary = ""
candidateVotes = {}
candidateList = []


' open the file for reading'
with open(csvpath, 'r', encoding="utf-8") as electionData:

    ' create the reader object'
    csvreader = csv.reader(electionData) 

    'skips the header row'
    firstRow = next(csvreader)

    ' loop to go through rows'
    for row in csvreader:
        ' get the total number of votes'
        totalVotes += 1

        ' check for candidate name '
        if row[2] not in candidateList:
            ' add name to list if not there'
            candidateList.append(row[2])

            ' set the total of that candidates vote count to 1 '
            candidateVotes[row[2]] = 1

        else:
            ' add 1 to existing candidate count'
            candidateVotes[row[2]] += 1

''
for oneCandidate in candidateVotes:
    ' retrieve vote count '
    numberVotes = candidateVotes.get(oneCandidate)
    ' calculate vote percentage '
    percentVotes = (float(numberVotes)/ float(totalVotes))
    ' add candidates with attributes to summary'
    voteSummary += f"{oneCandidate}: {percentVotes:.3%} ({numberVotes}) \n"

' get the candidate with the most votes'    
winnerWinner = max(candidateVotes, key=candidateVotes.get)

countRows = (f"\nElection Results \n"
    f"----------------------- \n"
    f"Total Votes: {totalVotes} \n"
    f"----------------------- \n"
    f"{voteSummary}"
    f"----------------------- \n"
    f"Winner: {winnerWinner} \n"
    f"----------------------- \n"
    )
print(countRows)

' export the file as txt'
with open(electionText, "w") as textFile:
    textFile.write(countRows)