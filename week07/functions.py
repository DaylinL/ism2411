# Self-Assessment Answers
# 1. I found the bugs by checking the code and looking at what was wrong.
#    The total was being replaced instead of added, the for loop was
#    missing a colon, and the while loop went one index too far.
#    This shows me that I need to read error messages and check each line.
#
# 2. apply_discount(price, tier) takes a price and a discount tier.
#    It subtracts the discount for that tier and returns the discounted price.
#    A colleague can use it by providing a price and a tier.
#
# AI Disclosure: I used ChatGPT to help explain the assignment, identify
# the bugs in Exercise 5, and organize the Python functions. I reviewed
# the code and should make sure I understand how each part works.


# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price - (price * discount)


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---

discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax = calculate_tax(discounted_price, 0.07)
total_after_tax = discounted_price + tax
print(f"After tax: ${total_after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(
    f'final_price(200, "gold", 0.07) = '
    f'${final_price(200, "gold", 0.07):.2f}'
)


# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---

# Bug fixes:
# 1. Add each sale to total instead of replacing total.
# 2. Add a colon at the end of the for loop line.
# 3. Use i < len(sales) so the loop does not access an invalid index.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---

x = 100  # Global variable


def double_it():
    x = 999  # Local variable; this is different from global x.
    return x * 2


print(x)            # Prints 100
print(double_it())  # Prints 1998
print(x)            # Prints 100 again

# Scope means a variable belongs to the part of the code where it is defined.
# The x inside double_it() is local, so it does not change the global x.
