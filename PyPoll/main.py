import os
import csv

PYPoll_CSV = os.path.join(os.getcwd(),'Resources', 'election_data.csv')
with open(PYPoll_CSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    i = 0
    per_votes = []
    votes = {}

    for row in csvreader:
        if i == 0:
            i += 1
            continue
        if row[2] in votes.keys():
            votes[row[2]]+=1
        else:
            votes[row[2]]=1
    total = sum(votes.values())
    for can in votes.keys():
        v_per = (votes[can]/total)
        percentage = "{:.2%}".format(v_per)
        per_votes.append(percentage)
        max_votes= max(votes.values())
        max_keys = [can for can, v in votes.items() if v == max_votes]
        zipped = zip(votes.keys(), votes.values(), per_votes)
print("Election Results")
print("------------------")
print(f"Total votes: {sum(votes.values())}")
print("---------------------")
for key, value, per_votes in zipped:
    print(key, value, per_votes)
print("--------------------------------------")
print(f"Winner is {max_keys} by {max_votes} votes")
print("--------------------------------------"