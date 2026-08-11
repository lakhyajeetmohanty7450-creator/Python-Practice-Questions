# Take numbers as input from the user one by one. Skip negative
# numbers and keep adding the positive ones. Stop when the user
# enters 0 and print the total. (Uses both continue and break.)

total = 0

i = 0
while i <5:
    num = int(input("Enter your number: "))

    if num<0:
        print("negative number not allow only + number")
        i += 1
        continue
    elif num >0:
        total += num
    elif num == 0:
        break


    i += 1

print(total)
