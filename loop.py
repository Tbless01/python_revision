capital_invested = int(input("Amount to invest: "))
number_of_years = int(input("How many years? "))
return_on_investment = capital_invested
for i in range(1, number_of_years + 1, 1):
    return_on_investment += return_on_investment * 0.05
    print("Year", i, "ROI is", f"{return_on_investment:.2f}")
