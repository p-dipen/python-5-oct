# Modularizing Code 
# create function which count mortage payments per month based on principle amount and years and default interest set in the function

def calculate_monthly_payment(principal: float, years: int):
    ANNUAL_INTEREST_RATE: float = 6.5

    # TODO: Handle Value error (user can insert negative values)

    total_months = years * 12

    monthly_rate = round((ANNUAL_INTEREST_RATE / 100) / 12,7)
    
    compound_factor =  round((1 + monthly_rate) ** total_months,4)

    monthly_payment = (principal * monthly_rate * compound_factor) / (compound_factor - 1)

    return round(monthly_payment,2)


# print(calculate_monthly_payment(40000, 2))