# 2nd part python-challenge

# Defining dependencies
import csv
import os

# Reading file
election_csv = os.path.join("resources", "election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Defining variables
count_votes = 0
total_votes = 0

# List and dictionaries
candidates = []
votes_per_candidate = {}

winner = ("")

# Main program

print(f"\n\tCount per candidate\n")

with open(election_csv) as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader, None)

    for each_line in csv_reader:
        total_votes += 1
        candidate = each_line[2]

        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 0
        votes_per_candidate[candidate] += 1

    for candidate in votes_per_candidate:
        vote_counter = votes_per_candidate.get(candidate)
        percent = float(vote_counter/total_votes)*100
        if vote_counter > count_votes:
            count_votes = vote_counter
            winner = candidate
        print(candidate, "|", "{:,.2%}".format(percent/100), "|", "{:,.0f}".format(vote_counter))
        

print(f"\n\tElection Results\n")
print("------------------------------------")
print(f"\nFinal vote count:{total_votes}\n")
# print(candidate, "|", "{:,.2%}".format(percent/100), "|", "{:,.0f}".format(vote_counter))
print(f"Winner Candidate: {winner}\n")

# Saving the output in Pypoll_output file on outputs folder
output_path = os.path.join("../outputs", "PyPoll_output")
with open(output_path, "w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write("------------------------------------")
    txtfile.write(f"\nFinal vote count:{total_votes}\n")
    for candidate in votes_per_candidate:
        vote_counter = votes_per_candidate.get(candidate)
        percent = float(vote_counter/total_votes)*100
        if vote_counter > count_votes:
            count_votes = vote_counter
            winner = candidate
        txtfile.write(f"\n{candidate, percent, vote_counter}\n")
    txtfile.write(f"\nWinner Candidate: {winner}\n")
