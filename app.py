# Inputs from image
on_road_price = 1726297     
down_payment = 173000     
interest_rate = 9.8     
loan_years = 4             

# Calculated values
loan_amount = on_road_price - down_payment
monthly_interest_rate = interest_rate / 12 / 100
num_months = loan_years * 12

# EMI formula using operators only:
# EMI = [P * r * (1 + r)^n] / [(1 + r)^n – 1]
P = loan_amount
r = monthly_interest_rate
n = num_months

compound_rate = (1 + r) ** n
numerator = P * r * compound_rate
denominator = compound_rate - 1
emi = numerator / denominator
total_payable = emi * n
print(f"Loan Amount    :  {loan_amount}")
print(f"Monthly EMI      : { round(emi)}")
print(f"Total Payable    : { round(total_payable)}")
