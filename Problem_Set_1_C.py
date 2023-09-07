annual_salary = float(input("Enter your annual salary: "))

semi_annual_raise = 0.07
investment_annual_rate = 0.04
down_payment = 0.25
house_cost = 1000000.0

current_savings = 0.0
month = 0

money_required = house_cost * down_payment

low = 0.0
high = 1.0
savings_rate = ((low + high) / 2.0)
previous_savings_rate = savings_rate
bisections = 0

def calc_savings(current_savings, annual_salary, savings_rate, month):
    for i in range(36):
        current_savings = current_savings + ((current_savings * investment_annual_rate)/ 12)
        current_savings = current_savings + ((annual_salary/12) * savings_rate)

        if (month % 6 == 0) and month > 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)

        month = month + 1
    return(current_savings)


while abs(current_savings - money_required) >= 100:
    current_savings = calc_savings(current_savings, annual_salary, savings_rate, 0)
    
    if current_savings < money_required:
        low = savings_rate
        current_savings = 0.0

    else:
        high = savings_rate
        current_savings = 0.0

    savings_rate = ((low + high) / 2.0)

    if round(savings_rate, 4) == round(previous_savings_rate,4):
        break
    else:
        previous_savings_rate = savings_rate
        bisections +=1


    # if bisections > 50:
    #     break
    # else:
    #     bisections += 1


if savings_rate > 0.9999:
    print("It is not possible to pay the down payment in three years")
else:
    print("Best savings rate:", round(savings_rate, 4))
    print("Steps in bisection search:", bisections)

