#Import dependencies
import os
import csv

#Read csv file
csv_file = os.path.join('Resources','election_data.csv')

with open(csv_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    data = []
    #create variables
    total_votes = 0
    cand_dict = {
        "name": [],
        "votes":[],
        "percents":[]
    }
    winner = ''
    winner_index = 0
    output = ''

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data (each vote) after the header
    for row in csvreader:
        #store data
        data.append(row)
        #start candidate list
        if not cand_dict["name"]:
            cand_dict["name"].append(data[total_votes][2])
            cand_dict["votes"].append(0)
            cand_dict["percents"].append(0)
        #create cand_match and cand_index for this vote
        cand_match = False
        cand_index = 0
        #search to see if unique candidate
        for name in cand_dict["name"]:
            if data[total_votes][2] == name:
                cand_match = True
                break
            else:
                cand_index += 1
        #tally votes for non-unique
        if cand_match:
            cand_dict["votes"][cand_index]+=1
        #add unique candidate
        else:
            cand_dict["name"].append(data[total_votes][2])
            cand_dict["votes"].append(0)
            cand_dict["percents"].append(0)

        #increase total_votes
        total_votes += 1
    
    #find winner and calculate percentages
    for i in range(0,len(cand_dict["name"])):
        #find winner
        if cand_dict["votes"][i]>cand_dict["votes"][winner_index]:
            winner_index = i
        #calculate percents
        cand_dict["percents"][i] = float(cand_dict["votes"][i])/float(total_votes)

#create candidate output string
for i in range(0,len(cand_dict["name"])):
    output += f'{cand_dict["name"][i]}: {cand_dict["percents"][i]:.3%} ({cand_dict["votes"][i]})\n'

#output
print('Election Results')
print('----------------------')
print(f'Total Votes: {total_votes}')
print('----------------------')
print(output, end = '')
print('----------------------')
print(f'Winner: {cand_dict["name"][winner_index]}')
#export text file
with open('Analysis/Analysis.txt', 'w') as writer:
    writer.write(
        'Election Results\n'
        '----------------------\n'
        f'Total Votes: {total_votes}\n'
        '----------------------\n'
    )
    writer.write(output)
    writer.write(
        '----------------------\n'
        f'Winner: {cand_dict["name"][winner_index]}'
    )