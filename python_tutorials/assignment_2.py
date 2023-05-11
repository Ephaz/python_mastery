import math

portion_down_payment = 0.25
current_savings = 0
r = 0.04    #interest on savings
current_savings = r * current_savings
annual_salary = float(input("How much is your annual salary?"))
total_cost = float(input("How much is your dream home?"))
portion_saved = float(input("What percentage of your salary would you like to save?"))

x = annual_salary/12 

current_savings = x + current_savings * r

amount_required_to_save = portion_down_payment * total_cost

print(amount_required_to_save/x)

