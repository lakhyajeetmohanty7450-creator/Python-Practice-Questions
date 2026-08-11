# . Write a function fizzbuzz(n) that takes a single number and prints
# "Fizz" if it's divisible by 3,"Buzz" if it's divisible by 5,"FizzBuzz"
# if it's divisible by both, otherwise print the number itself.

def fizzbuzz(n):
    if n % 3 ==0 and not n%5 ==0 : 
        return "Fizz"
    elif n%5 == 0 and not n%3 == 0:
        return " Buzz"
    elif n%3 == 0 and n%5 ==0:
        return "FIZZBUZZ"
    else:
        return n

number = int(input("Enter your number: "))
print(fizzbuzz(number))