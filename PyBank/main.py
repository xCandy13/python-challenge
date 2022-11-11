#Import dependencies
import os
import csv

#Read csv file
csv_file = os.path.join('Resources','budget_data.csv')

with open(csv_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    data = []
    #create variables
    months = 0
    total = 0.0
    changes=[]
    avg_changes = 0.0
    max_inc_index = 0
    max_dec_index = 0

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        #store data
        data.append(row)
        
        #add profit/loss to total
        total = total+float(row[1])
        #count rows (months)
        months += 1

    #calculate changes, store in array changes[], find min/max change
    for i in range(1,len(data)):
        #calculate change
        number = float(data[i][1])-float(data[i-1][1])
        
        #store change
        changes.append(number)

        #compare change to min/max
        if number>changes[max_inc_index]:
            max_inc_index = i-1
        elif number<changes[max_dec_index]:
            max_dec_index = i-1
    #calculate avg_changes
    avg_changes = sum(changes)/(months-1)
    
    
#output
print('Financial Analysis')
print('----------------------')
print(f'Total Months: {months}')
print(f'Total Profit/Loss: ${total:.2f}')
print(f'Average Change: ${avg_changes:.2f}')
print(f'Greatest Increase: {data[max_inc_index+1][0]} (${changes[max_inc_index]:.2f})')
print(f'Greatest Decrease: {data[max_dec_index+1][0]} (${changes[max_dec_index]:.2f})')

#export text file
with open('Analysis/Analysis.txt', 'w') as writer:
    writer.write(
        'Financial Analysis\n'
        '----------------------\n'
        f'Total Months: {months}\n'
        f'Total Profit/Loss: ${total:.2f}\n'
        f'Average Change: ${avg_changes:.2f}\n'
        f'Greatest Increase: {data[max_inc_index+1][0]} (${changes[max_inc_index]:.2f})\n'
        f'Greatest Decrease: {data[max_dec_index+1][0]} (${changes[max_dec_index]:.2f})\n'
    )
