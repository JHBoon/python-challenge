import os
import csv
#write headers
print("Election Results")
print()
print("-------------------------")

#open file with election information
csvpath = os.path.join("election_data.csv")
#loop to count rows = votes.
row_count = -1
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        row_count += 1
        if "" in row:
            break

print("Total votes: ", row_count)
print("-------------------------")

#prepare dictoniaries
vote_counts = 0
candidates = []
candidates_votes = {}

election_data_csv = os.path.join("election_data.csv")
with open(election_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")

        #skip header
        next(csvreader)

        #loop line by line to gather data needed
        for row in csvreader:
                
                #number of total votes
            vote_counts += 1

                #check if  the name is already logged
            if  row[2] not in candidates:
                    #if the name isn't logged yet,  ad them to the lost and start vote count
                candidates.append(row[2])
                candidates_votes[row [2]] = 1
                #if the name is already on the list, just increase their vote count
            else:
              candidates_votes[row[2]] += 1
    
#sort the candidates aplhabetically
sorted_candidates =sorted (candidates)

for candidate in sorted_candidates:
    percentage = (candidates_votes[candidate] / vote_counts) * 100
    print(f"{candidate}: {percentage:.3f}% ({candidates_votes[candidate]})")
    print("-------------------------")

# Find the winner
winner = max(candidates_votes, key=candidates_votes.get)

# Print the winner's information
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export the output to an txt file
with open("Election Results Analysis.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes:{row_count}\n")
    file.write("-------------------------\n")
#find candidates, percentage votes and total votes
    for candidate in sorted_candidates:
        percentage = (candidates_votes[candidate]/vote_counts)*100
        file.write(f"{candidate}:{percentage:.3f}% ({candidates_votes[candidate]})\n")

    file.write("-------------------------\n")
    
    # Find the winner
    winner = max(candidates_votes, key=candidates_votes.get)
    
    # Write the winner's information to the file
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")



