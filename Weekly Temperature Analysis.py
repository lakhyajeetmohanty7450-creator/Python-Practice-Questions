# Write a Python program to store the temperatures of seven days 
# and display the highest temperature, lowest temperature, and average temperature

print("This last seven day temperatures chat")
list1 =[]

i = 0
while i < 7:
    temp = int(input("Enter your each day temperatures: "))
    list1.append(temp)
    i += 1

print(f"Each day temperatures {list1}")
print(f" Highest temperature {max(list1)}")
print(f"Lowest temperature { min(list1)}")
print(f"Average temperature { sum(list1)/len(list1)}")