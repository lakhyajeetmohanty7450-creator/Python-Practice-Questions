# Write a function power(base, exp) that returns base raised to exp using a
# loop - no ** operator or pow() allowed.

def  power(base, exp):
    result = 1
    i =0
    while i < exp:
        result *= base
        i+=1


    return result


a = int(input("Enter your base number: "))
b = int(input("Enter your exp number: "))
print(power(a,b))  