#  Get keys by the help of values
student={ "luna":90,"jagu":89,"mohal":87,"kiran":88 }

a = int(input("Enter your values: "))

for keys,values in student.items():
    if values == a:
        print(keys)