import time as t
# Ask the user for the original price of the item
original_price = float(input("Enter the original price of the item: $"))
# Get the user's input for the state they are in
state = input("What state are you in? (Use the abbreviation, which \nyou can find in the file 'state_abbrev.txt') --> ")

# Define a dictionary to store the sales tax rates for each state
sales_tax_rates = {
    'AL': 0.04,
    'AK': 0.05,
    'AZ': 0.0625,
    'AR': 0.07,
    'CA': 0.0825,
    'CO': 0.03,
    'CT': 0.0635,
    'DE': 0.06,
    'FL': 0.07,
    'GA': 0.05,
    'HI': 0.04,
    'ID': 0.06,
    'IL': 0.07,
    'IN': 0.07,
    'IA': 0.06,
    'KS': 0.065,
    'KY': 0.06,
    'LA': 0.0975,
    'ME': 0.055,
    'MD': 0.06,
    'MA': 0.0625,
    'MI': 0.06,
    'MN': 0.07,
    'MS': 0.07,
    'MO': 0.04225,
    'MT': 0.06,
    'NE': 0.055,
    'NV': 0.0685,
    'NH': 0.06,
    'NJ': 0.07,
    'NM': 0.07125,
    'NY': 0.0845,
    'NC': 0.07,
    'ND': 0.05,
    'OH': 0.0575,
    'OK': 0.065,
    'OR': 0.07,
    'PA': 0.06,
    'RI': 0.07,
    'SC': 0.06,
    'SD': 0.04,
    'TN': 0.07,
    'TX': 0.0625,
    'UT': 0.06,
    'VT': 0.06,
    'VA': 0.053,
    'WA': 0.065,
    'WV': 0.06,
    'WI': 0.05,
    'WY': 0.04
}
state = state.upper()
# Use the user's input and the dictionary to calculate the sales tax rate
if state in sales_tax_rates:
    sales_tax_rate = sales_tax_rates[state]
else:
    print("Invalid state")
    exit()


# Calculate the total cost with sales tax
total_cost = original_price * (1 + sales_tax_rate)
rounded_total = round(total_cost, 2)

print(f"The total cost with sales tax in {state} is ${total_cost}")
t.sleep(5) #When compiled to EXE, prevents the program from closing before printing the output.
