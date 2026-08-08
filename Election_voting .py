# Create a command-line Election Voting System using Python. 
# The program should allow users to cast votes for candidates, 
# display the election results, and announce the winner.

candidates={"Alice": 7,"Bob": 1, "Charlie": 5}
voter = []

def voting():
    voter_id = int(input("Enter your voter id: "))
    if voter_id in voter:
        print("You vote is already add you cannot vote 2nd time")
    else:
        print(f"This is candidates list {list(candidates.keys())}")
        choose = input("Enter your Choose candidates: ")
        if choose in candidates:
            voter.append(voter_id)
            candidates[choose] +=1
            print("Your vote is now successfully submited")
            print(f"your voter ID {voter_id}")
        else:
            print("Invalid candidate name")
        
    return


def winner():
    
    a=list(candidates.values())
    max_ =max(a)
    
    for key , value in candidates.items():
        if value == max_:
            return(key)



while True:
    voting()

    chose = input("Do you want another person to vote? (yes/no): ")
    if chose == "no":
        break

print("Election Results")
print("----------------\n")
for a,b in candidates.items():
    print(a,b)

print(f"Winner of this Election is {winner()}")



