income = float(input("What is your monthly income (in $)? "))
expenses = float(input("What are your monthly expenses (in $)? "))
age = int(input("What is your age? "))
risk_appetite = input("What is your risk appetite? (low/medium/high): ").lower()
savings = float(input("How much do you have in savings (in $)? "))
debt = float(input("What is your total debt (in $)? "))
emergency_fund = float(input("How much have you saved for emergency fund (in $)? "))

savings_ratio = (savings / (income * 12)) * 100  # % of yearly income
debt_ratio = (debt / (income * 12)) * 100        # % of yearly income
monthly_savings = income - expenses
months_expenses_in_emergency_fund = emergency_fund / expenses if expenses > 0 else 0
