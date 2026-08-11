# Write a function tax_calculator(income) that takes annual income and returns
# the tax amount based on these slabs:

# Up to 2,50,000 → No tax
# 2,50,001 to 5,00,000 → 5%
# 5,00,001 to 10,00,000 → 20%
# Above 10,00,000 → 30%

def tax_calculator(income):
    if income <= 250000 :
        return "no tax"
    if income >= 250001 and income <= 500000:
        print("%5 tax")
        tax = (5/100)*income
        print("Amount of tax ")
        return tax
    elif income >= 500001 and income < 1000000:
        print("%20 tax")
        tax1 = (20/100)*income
        print("Amount of tax")
        return tax1
    elif income >= 1000000:
        print("%30 tax")
        tax2 = (30/100)*income
        print("Amount of tax")
        return tax2


inc = int(input("Enter your income:"))
print(tax_calculator(inc))
        
