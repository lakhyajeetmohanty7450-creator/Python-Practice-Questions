# Write a Python program to store the daily sales of a shop 
# for one week and display the total sales, highest sale, lowest sale, and Average sale.

print("The daily sales of a shop for one week ")
list1=[]
i = 1
while i <= 7:
    sales = int(input(f"Enter your sale in day {i}: "))
    list1.append(sales)
    i += 1

print(f"Total sales: {sum(list1)}")
print(f"Highest sale: {max(list1)}")
print(f"Lowest sale: {min(list1)}")
print(f"Average sale: {sum(list1)/len(list1)}")


