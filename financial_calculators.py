"""
A short program that allows users to select from two financial calculators.
    1. An investment calculator
    2. A home loan (mortgate/bond) repayment calculator
Users are prompted to make selections and input data.
Program calculates and returns results in a user-friendly manner.
Error handling ensure smooth operation.
"""

import math

# Print calculator type options - Investment or Bond
print(
    "\ninvestment\t- to calculate the amount of interest you'll earn on your "
    "investment"
)
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")

# Get user calculator type choice
while True:
    calc_choice = input(
        "\nEnter either 'investment' or 'bond' from the menu above to "
        "proceed: "
    ).lower()
    if calc_choice == "investment":
        print("\nThank you for choosing the Investment Calculator.")
        break
    elif calc_choice == "bond":
        print("\nThank you for choosing the Bond Calculator.")
        break
    else:
        print("\nI'm sorry, I didn't understand that.")

# Get user currency - used in both calculators
currency = input("\nPlease enter your currency:\t\t\t\t")


# Investment calculator

# Check for 'investment' choice
if calc_choice == "investment":

# Get user Investment deposit amount
    while True:
        deposit_amount = input(
            f"Please enter the amount in {currency} you plan to invest:\t"
        )
        try:
            deposit_amount = float(deposit_amount)
            break
        except ValueError:
            print("Please enter only numbers.")

# Get user Investment interest rate
    while True:
        interest_rate = input("Please enter the % rate of interest: \t\t\t")
        try:
            interest_rate = float(interest_rate)
            break
        except ValueError:
            print("Please enter only numbers.")

# Get user investment term in years
    while True:
        term_years = input("Please enter the investment term in years:\t\t")
        try:
            term_years = int(term_years)
            break
        except ValueError:
            print("Please enter only whole numbers.")

# Print Investment interest type options - simple or compound
    print(
        "\nsimple interest \t- is calculated annually on the initial amount "
        "of investment"
    )
    print(
        "compound interest\t- is calculated annually on the current amount "
        "in the investment"
    )

# Get user Investment interest type choice
    while True:
        interest_type = input(
            "\nEnter either 'simple' or 'compound' to proceed:\t\t"
        ).lower()
        if interest_type in ["simple", "compound"]:
            break
        print("\nI'm sorry, I didn't understand that.")

# Calculate Investment interest according to user choice
    if interest_type == "simple":
        interest = deposit_amount * ( 1 + (interest_rate / 100) * term_years)
    elif interest_type == "compound":
        interest = deposit_amount * math.pow(1 + (interest_rate / 100),
                                            term_years)

# Calculate Investment interest only
    interest_only = interest - deposit_amount

# Return the Investment Calculator values
    print("\nThank you.")
    print(
        f"\nWith {interest_type} interest, your initial investment of "
        f"{currency}{str(round(deposit_amount,2))} over a {term_years} year "
        "term will:" 
        )
    print(
        "\nGive a total return on investment of:\t\t\t"
        f"{currency}{str(round(interest,2))}"
    )
    print(
        "Including an interest amount of:\t\t\t"
        f"{currency}{str(round(interest_only,2))}"
    )


# Bond calculator

# Check for 'bond' choice
if calc_choice == "bond":

# Get Bond user house value
    while True:
        house_value = input(
            f"Please enter the present house value in {currency}:\t\t"
        )
        try:
            house_value = float(house_value)
            break
        except ValueError:
            print("Please enter only numbers.")

# Get user Bond interest rate
    while True:
        interest_rate = input("Please enter the % rate of interest: \t\t\t")
        try:
            interest_rate = float(interest_rate)
            break
        except ValueError:
            print("Please enter only numbers.")

# Get user Bond investment term in months
    while True:
        term_months = input(
            "Please enter the repayment period in months:\t\t"
        )
        try:
            term_months = int(term_months)
            break
        except ValueError:
            print("Please enter only whole numbers.")

# Calculate Bond repayment amount
    month_interest = (interest_rate / 100) / 12
    repayment = (
        (month_interest * house_value)
        / (1 - (1 + month_interest) ** (- term_months))
    )

# Calculate total Bond cost
    total_bond = repayment * term_months

# Calculate Bond interest only
    interest_only = total_bond - house_value

# Return the calculated Bond Calculator values
    print("\nThank you.")
    print(
        f"\nFor a bond value of {currency}{str(round(house_value,2))}, "
        "repaid over {term_months} months at an interest rate of "
        f"{interest_rate}%: "
    )
    print(
        "\nYour monthly repayments will be \t\t\t"
        f"{currency}{str(round(repayment,2))}"
    )
    print(
        "This bond will cost you a total of:\t\t\t"
        f"{currency}{str(round(total_bond,2))}"
    )
    print(
        "Including an interest amount of:\t\t\t"
        f"{currency}{str(round(interest_only,2))}"
        )

print("\nThank you for using this calculator. Have a nice day.")
