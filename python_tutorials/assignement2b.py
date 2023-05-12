house_portion_down_payment = 0.25
annual_salary = float(input("How much is your annual salary? > "))
portion_of_salary_to_contribute = float(input("What percentage of your salary would you like to save? > " ))
total_cost_of_house = float(input("How much is your dream home? > "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal >"))

#interest on savings
r = 0.04/12

#amount required to save or the down payment amount
amount_required_to_save = house_portion_down_payment * total_cost_of_house

#the current savings are zero, therefore it starts here
current_savings = 0

#This is the number of months that one should save for down payment
number_of_months = 0

while current_savings < amount_required_to_save:
    monthly_salary_contribution = (annual_salary/12) * portion_of_salary_to_contribute
    current_savings += monthly_salary_contribution + current_savings * r
    number_of_months += 1
    
    #this loop updates the annual salary every 6 months 
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        
    #print the number of monts required to save to afford the deposit        
print(f"Number of months:{number_of_months}")