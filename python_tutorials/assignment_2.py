
house_portion_down_payment = 0.25
annual_salary = float(input("How much is your annual salary? > "))
total_cost_of_house = float(input("How much is your dream home? > "))
portion_of_salary_to_contribute = float(input("What percentage of your salary would you like to save? > " ))

#interest on savings
r = 0.04/12

#x is the amount contributed every month
x = (annual_salary/12) * portion_of_salary_to_contribute 

#amount required to save or the down payment amount
amount_required_to_save = house_portion_down_payment * total_cost_of_house

#the current savings are zero, therefore it starts here
current_savings = 0
#This is the number of months that one should save for down payment
number_of_months = 0

while current_savings < amount_required_to_save:
    current_savings += x + current_savings * r
    number_of_months += 1

#print the number of monts required to save to afford the deposit        
print(f"Number of months:{number_of_months}")
