import math

house_portion_down_payment = 0.25
current_savings = 0
r = 0.04/12    #interest on savings
current_savings = r * current_savings
annual_salary = float(input("How much is your annual salary?"))
total_cost = float(input("How much is your dream home?"))
portion_saved = float(input("What percentage of your salary would you like to save?"))/100

x = annual_salary/12 

amount_required_to_save = house_portion_down_payment * total_cost

current_savings = (x + current_savings) * (1+r)

print(current_savings)

contributions = []

print (contributions)

while contributions < amount_required_to_save:
    contributions += (x + current_savings) * (1+r)
    print(contributions)
   
total_months = amount_required_to_save/(contributions)

print(total_months)
print(contributions)