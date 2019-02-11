



# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

   Correy = 0
   Khan = 0
   Li = 0
   OTooley = 0
   sum_vote = 0

   for row in csvreader:
       next(csvreader)

       # A complete list of candidates who received votes and
       # The total number of votes each candidate won
       
       if row[2] == "Correy":
           Correy = Correy + 1
       elif row[2] == "Khan":
           Khan = Khan + 1
       elif row[2] == "Li":
           Li = Li + 1
       elif row[2] == "O'Tooley":
           OTooley = OTooley + 1

       # The total number of votes cast
       sum_vote = sum_vote + 1

       # The percentage of votes each candidate won
       Khan_percentage = Khan / sum_vote
       Correy_percentage = Correy / sum_vote
       Li_percentage = Li / sum_vote
       OTooley_percentage = OTooley / sum_vote

       # The total number of votes each candidate won




       # The winner of the election based on popular vote.






   print("Khan: " + str(Khan))
   print("Correy: " + str(Correy))
   print("Li: " + str(Li))
   print("O'Tooley: " + str(OTooley))
   print(sum_vote)

   print("Khan: " + str(Khan_percentage))
   print("Correy: " + str(Correy_percentage))
   print("Li: " + str(Li_percentage))
   print("O'Tooley: " + str(OTooley_percentage))




output_path = os.path.join("Output", "PyPoll_output")
with open(output_path, 'w', newline="") as csvfile:
   csvwriter = csv.writer(csvfile, delimiter=",")

   csvwriter.writerow(["Election Results"])
   csvwriter.writerow(["-------------------------"])
   csvwriter.writerow(["Total Votes: ", sum_vote])
   csvwriter.writerow(["-------------------------"])
   csvwriter.writerow(["Khan: "])
   csvwriter.writerow(["Correy: "])
   csvwriter.writerow(["Li: "])
   csvwriter.writerow(["O'Tooley: "])
   csvwriter.writerow(["-------------------------"])
   csvwriter.writerow(["Winner: "])