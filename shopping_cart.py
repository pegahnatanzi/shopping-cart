# shopping_cart.py

import datetime as date

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] 
# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


# INFO CAPTURE / INPUT: capture product ids until we're done
    # (use infinite while loop)

tax_percentage = 0.0875  # note: this is given as NYC tax rate

checkout_start_date_time = date.datetime.now()

subtotal_price = 0

selected_ids = []


while True:
    selected_id = input("Please select / scan a valid product id: ")
    if selected_id.upper() == "DONE":
        break        # this means, if input is DONE, stop the loop
    else:
        selected_ids.append(selected_id)
        # maybe display the selected product's name and price here/now



# INFO DISPLAY / OUTPUT: Perform product lookups to determine what the product's name and price are

# First, we want to print the following info at top of receipt:
    # A grocery store name of your choice
    # A grocery store phone number and/or website URL and/or address of choice
    # The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM): https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

print("Fleeb's Market")
print("PHONE NUMBER: 310-818-2652")
print("26 Fleeb Street, FleebsVille, CA 90210")
print("CHECKOUT TIME:" + checkout_start_date_time.strftime("%Y-%m-%d %I:%M %p")))
print("___________________________________")


# Given function to properly format prices:
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


for selected_id in selected_ids:
    #print(selected_id)
    # lookup the corresponding product!
    # ... and display the selected product's name and price
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    # FYI the result of our list comprehension will be a list!
    matching_product = matching_products[0] # ... so we'll need to access its first item using [0]
    subtotal_price = subtotal_price + matching_product["price"]
    print("SELECTED PRODUCT: " + matching_product["name"] + " " + to_usd(matching_product["price"]))


# we need to have program add up all of the prices & apply the tax rate: 

tax = subtotal_price * tax_percentage

total_price = subtotal_price + tax


# now, display the rest of receipt content:
    # The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
    # The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
    # The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
    # A friendly message thanking the customer and/or encouraging the customer to shop again

print("SUBTOTAL: " + to_usd(subtotal_price))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total_price))
print("___________________________________")
print("Thanks for shopping at Fleeb's Market! See you next time!")