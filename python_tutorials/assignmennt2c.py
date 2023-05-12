import math

semi_annual_raise = 0.07
r = 0.04
total_cost_of_house = 1000000
down_payment = 0.25 * total_cost_of_house
months = 36
epsilon = 100

low = 0
high = 1
guess_rate = (low + high) / 2

x = float(input("Enter, the starting salary > "))

while True:
    current_savings = 0
    
    for month in range(1, months + 1):
        annual_salary = x
        if month % 6 == 0:
            annual_salary *= (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * guess_rate
        current_savings *= 1 + r / 12
        current_savings += monthly_savings
    if abs(current_savings - down_payment) < epsilon:
        break
    elif current_savings < down_payment:
        low = guess_rate
    else:
        high = guess_rate
    guess_rate = (low + high) / 2

print("Best savings rate:", round(guess_rate, 4))
print("Steps in bisection search:",abs(round(math.log(high - low, 2), 0)))
