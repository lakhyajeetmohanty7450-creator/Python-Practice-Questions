# Write a Python program to store daily expenses for one week 
# and display the total expense, highest expense, lowest expense, and average expense.
list1 =[]
i = 1
while i <= 7:
    exp = int(input(f"Enter your day {i} expenses: "))
    list1.append(exp)
    i += 1

print(f"Total expense {sum(list1)}")
print(f"Highest expense {max(list1)}")
print(f"Lowest expense {min(list1)}")
print(f"Average expense {sum(list1)/len(list1)}")
