# Part B: Saving, with a raise

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
month = 0

money_required = total_cost * portion_down_payment

while current_savings < money_required:
    current_savings = current_savings + ((current_savings * 0.04)/ 12)
    current_savings = current_savings + ((annual_salary/12) * portion_saved)

    if (month % 6 == 0) and month > 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

    month = month + 1

    if current_savings >= money_required:
        print("Number of months:", month)
        break
    else:
        continue