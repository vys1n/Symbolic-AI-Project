print("Welcome to the Finance Expert System")
print("Answer the following questions:\n")

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

print("\nFinance Recommendations\n")

# Savings Advice
if monthly_savings <= 0:
    print("You are spending more than you earn. Reduce expenses immediately.")
elif savings_ratio < 20:
    print("Your savings ratio is low. Aim to save at least 20% of your income.")
elif savings_ratio >= 30:
    print("You have a strong savings habit. Keep it up!")

# Investment Advice
if risk_appetite == "high" and age < 40:
    print("Recommended Investments: Stocks, Mutual Funds, Index Funds")
elif risk_appetite == "medium":
    print("Recommended Investments: Balanced Mutual Funds, Bonds")
elif risk_appetite == "low" or age > 50:
    print("Recommended Investments: Fixed Deposits, Gold, Government Bonds")

# Debt Advice
if debt_ratio > 40:
    print("Your debt ratio is too high. Consider debt consolidation or reducing loans.")
elif debt_ratio < 20:
    print("Your debt is at a safe level. Maintain discipline.")

# Emergency Fund Advice
if months_expenses_in_emergency_fund < 6:
    print("Build your emergency fund to cover at least 6 months of expenses.")
else:
    print("Your emergency fund is adequate.")

# Final Recommendation
if monthly_savings > 0 and savings_ratio > 20 and months_expenses_in_emergency_fund >= 6:
    print("\nOverall: You are on the right financial track! Keep investing and diversifying.\n")
else:
    print("\nOverall: Focus on improving savings, reducing debt, and building emergency funds.\n")
