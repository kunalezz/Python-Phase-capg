
units_consumed = int(input().strip())

# Initialize total bill
total_bill_amount = 0

# Calculate bill based on slabs
if units_consumed <= 100:
    total_bill_amount = units_consumed * 5

elif units_consumed <= 300:
    first_hundred_units_cost = 100 * 5
    remaining_units = units_consumed - 100
    next_units_cost = remaining_units * 7

    total_bill_amount = first_hundred_units_cost + next_units_cost

else:
    first_hundred_units_cost = 100 * 5
    next_two_hundred_units_cost = 200 * 7
    remaining_units = units_consumed - 300
    above_three_hundred_cost = remaining_units * 10

    total_bill_amount = (
        first_hundred_units_cost
        + next_two_hundred_units_cost
        + above_three_hundred_cost
    )

# Print result
print(total_bill_amount)