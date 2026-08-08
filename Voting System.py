# Write a Python program to create a simple voting system that stores the names of candidates 
# and the number of votes received by each candidate, then displays the winner.

total = int(input("Enter your total number of candidates: "))
list1 =[]
i = 0
while i < total:
    candi = input("Candidates names: ")
    votes = int(input(f"Totsl vote {candi} have: "))
    dict1 = {"candidates name" : candi , "votes take":votes}
    list1 .append(dict1)
    i += 1

winner = list1[0]
for a in list1:
    if a["votes take"] > winner["votes take"]:
        winner = a

winners =[]
for a in list1:
    if a["votes take"] == winner["votes take"]:
        winners.append(a["candidates name"])



if len(winners) == 1:
    print(f"Winner is {winners[0]}")
else:
    print("Draw between:")
    for i in winners:
        print(i)

    




