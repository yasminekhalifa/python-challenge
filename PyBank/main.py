import os
import csv

PYBANK_CSV = os.path.join(os.getcwd(),'Resources', 'budget_data.csv')
with open(PYBANK_CSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    total = i = 0
    maxm_profits = minm_profits = ["",""]
    for row in csvreader:
        if i == 0:
            i += 1
            continue
        if i==1:
           maxm_profits = minm_profits = row
        prLoss = int(row[1])
        total+=prLoss
        if prLoss > int(maxm_profits[1]):
            maxm_profits = row
        if prLoss < int(minm_profits[1]):
            minm_profits = row
        i+=1
    print(f"Financial Analysis") 
    print("--------------------")   
    print(f"Total Months: {i-1}")
    print(f"Total: ${total}")
    print(f"Average change: ${total/(i-1)}")
    print(f"Greatest increase in profits: {'  $'.join(maxm_profits)}")
    print(f"Greatest decrease in profits: {'  $'.join(minm_profits)}")

 



    
