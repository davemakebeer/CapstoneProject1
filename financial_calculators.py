# This is a customer-specific program that allows users to access two interest calculators:
#   1. An investment calculator
#   2. A home loan repayment calculator

"""Pseudocode

Import math functions

Print line briefly describing investment calculator function
Print line briefly describing bond calculator function

While True loop with if-elif-else block to determine user choice 'investment' or 'bond'.
    ask user to choose investment or bond, make lower case and store into the variable 'calc_choice'.
    if 'investment'
        return confirmation
        break
    elif 'bond'
        return confirmation
        break
    else
        return error message

Request user currency and store into the variable 'currency'.

-Investment calculator
Boolean if calc_choice is "investment"
    
    While True loop with try-except block to retrieve user deposit amount
        Request user deposit amount and store into the string variable 'deposit_amount'.
        try
            cast 'deposit_amount' to float
            return confirmation
            break
        except error
            return error message
    
    While True loop with try-except block to retrieve user interest rate
        Request user interest rate and store into the string variable 'interest_rate'.
        try
            cast 'interest_rate' to float
            return confirmation
            break
        except error
            return error message
        
    While True loop with try-except block to retrieve user investment term length in years
        Request user term_years and store into the string variable 'term_years'.
        try
            cast 'term_years' to integer
            return confirmation
            break
        except error
            return error message
    
    While True loop with if-elif-else block to determine user choice 'simple' or 'compound'.
        ask user to choose simple or compound, make lower case and store into the variable 'interest_type'.
        if 'simple'
            return confirmation
            break
        elif 'compound'
            return confirmation
            break
        else
            return error message
    
    While True loop with if-elif-else block to determine user choice 'simple' or 'compound' interest.
    ask user to choose simple or compoundd, make lower case and store into the variable 'interest_type'.
    if 'simple'
        break
    elif 'compound'
        break
    else
        return error message
    
    if "simple"
        interest = deposit_amount * ( 1 + (interest_rate/100)*term_years)
    if "compound"
        interest = deposit_amount * math.pow(1+(interest_rate/100),term_years)
    
    Subtract deposit_amount from interest and store into the variable 'interest_only'.
        
    Return summary of user information
    Return total return with currency
    Return interest amount with currency

-Investment calculator
Boolean if calc_choice is "bond"

    While True loop with try-except block to retrieve user house value
        Request user house value and store into the string variable 'house_value'.
        try
            cast 'house_value' to float
            return confirmation
            break
        except error
            return error message

   While True loop with try-except block to retrieve user interest rate
        Request user interest rate and store into the string variable 'interest_rate'.
        try
            cast 'interest_rate' to float
            return confirmation
            break
        except error
            return error message

    While True loop with try-except block to retrieve user investment term length in months
        Request user term_months and store into the string variable 'term_months'.
        try
            cast 'term_months' to integer
            return confirmation
            break
        except error
            return error message
            
    repayment = (interest_rate * house_value) / ( 1 - (1 + interest_rate) ** (- term_months))

    Subtract house_value from interest and store into the variable 'interest_only'.
        
    Return summary of user information
    Return monthly repayments with currency
    Return total cost of bond with currency
    Return interest amount with currency

Print 'thank you' line.
"""

# Import math functionality
import math

# User selection screen for calculator type with explanation
print("\ninvestment\t- to calculate the amount of interest you'll earn on your investment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")

# While True loop with if-elif-else block to idenify user choice
while True:
    calc_choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if calc_choice == "investment":
        print("\nThank you for choosing the Investment Calculator.")
        break
    elif calc_choice == "bond":
        print("\nThank you for choosing the Bond Calculator.")
        break
    else:
        print("\nI'm sorry, I didn't understand that.")

# Request user currency
currency = input("\nPlease enter your currency:\t\t\t\t")

# Investment calculator

# Check for 'investment' choice
if calc_choice == "investment":

# While True loop with try-except block to retrieve user deposit amount
    while True:
        deposit_amount = input(f"Please enter the amount in {currency} you plan to invest:\t")
        try:
            deposit_amount = float(deposit_amount)
            break
        except ValueError:
            print("Please enter only numbers.")

# While True loop with try-except block to retrieve user interest rate
    while True:
        interest_rate = input("Please enter the % rate of interest: \t\t\t")
        try:
            interest_rate = float(interest_rate)
            break
        except ValueError:
            print("Please enter only numbers.")

# While True loop with try-except block to retrieve user investment term in years
    while True:
        term_years = input("Please enter the investment term in years:\t\t")
        try:
            term_years = int(term_years)
            break
        except ValueError:
            print("Please enter only whole numbers.")

# User selection screen for interest type with explanation
    print("\nsimple interest \t- is calculated annually on the initial amount of investment")
    print("compound interest\t- is calculated annually on the current amount in the investment")

# While True loop with if-elif-else block to idenify type of interest
    while True:
        interest_type = input("\nEnter either 'simple' or 'compound' to proceed:\t\t").lower()
        if interest_type == "simple":
            break
        elif interest_type == "compound":
            break
        else:
            print("\nI'm sorry, I didn't understand that.")

# Check for interest, make appropriate calculation and store into the variable 'interest'. 
    if interest_type == "simple":
        interest = deposit_amount * ( 1 + (interest_rate/100)*term_years)
    elif interest_type == "compound":
        interest = deposit_amount * math.pow(1+(interest_rate/100),term_years)
    
# Calculate the interest as a separate variable
    interest_only = interest - deposit_amount

# Return the calculated values
    print("\nThank you.")
    print(f"\nWith {interest_type} interest, your initial investment of {currency}{str(round(deposit_amount,2))} over a {term_years} year term will:" )
    print(f"\nGive a total return on investment of:\t\t\t{currency}{str(round(interest,2))}")
    print(f"Including an interest amount of:\t\t\t{currency}{str(round(interest_only,2))}")

# Bond calculator

# Check for 'bond' choice
if calc_choice == "bond":

# While True loop with try-except block to retrieve user house value
    while True:
        house_value = input(f"Please enter the present house value in {currency}:\t\t")
        try:
            house_value = float(house_value)
            break
        except ValueError:
            print("Please enter only numbers.")

# While True loop with try-except block to retrieve user interest rate
    while True:
        interest_rate = input("Please enter the % rate of interest: \t\t\t")
        try:
            interest_rate = float(interest_rate)
            break
        except ValueError:
            print("Please enter only numbers.")

# While True loop with try-except block to retrieve user investment term in months
    while True:
        term_months = input("Please enter the repayment period in months:\t\t")
        try:
            term_months = int(term_months)
            break
        except ValueError:
            print("Please enter only whole numbers.")

# Calculate repayment amount
    month_interest = (interest_rate/100)/12
    repayment = (month_interest * house_value) / ( 1 - (1 + month_interest) ** (- term_months))

# Calculate total cost
    total_bond = repayment * term_months

# Calculate the interest as a separate variable
    interest_only = total_bond - house_value

# Return the calculated values
    print("\nThank you.")
    print(f"\nFor a bond value of {currency}{str(round(house_value,2))}, repaid over {term_months} months at an interest rate of {interest_rate}%: ")
    print(f"\nYour monthly repayments will be \t\t\t{currency}{str(round(repayment,2))}")
    print(f"This bond will cost you a total of:\t\t\t{currency}{str(round(total_bond,2))}")
    print(f"Including an interest amount of:\t\t\t{currency}{str(round(interest_only,2))}")

# Line of text to thank the user
print("\nThank you for using this calculator. Have a nice day.")
