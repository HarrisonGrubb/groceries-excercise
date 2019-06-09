# groceries.py

#from pprint import pprint

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
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# print(len(products))
# print(products[0])
# print(products[0]['name'])

# for item in range(0, len(products)):
#     print(products[item]['name'])

# alpha order
# names = []
# for item in range(0, len(products)):
#     names.append(products[item]['name'])
# names.sort()

# for item in names:
#     print(f"\n {item}")

#attributions ##########################################################
#lambda function courtesy of stackoverflow :)  
#https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

#set fix courtesy of stackoverflow :)
#https://stackoverflow.com/questions/7961363/removing-duplicates-in-python-lists

# format applier courtesy of Dan Gode's class financial statement analytics 
#attributions ##########################################################



def alpha_sorted_products(inventory):
    sorted_inventory = sorted(inventory, key = lambda k: k['name'])
    print('________________________________')
    print('There are', len(sorted_inventory), 'products')
    print('________________________________')
    for item in range(0,len(sorted_inventory)):
        print('+',sorted_inventory[item]['name'], "(${:,.2f})".format(sorted_inventory[item]['price']))

def alpha_sorted_departments(inventory):
    unique_departments = []
    for depts in range(0, len(inventory)):
        unique_departments.append(inventory[depts]['department'])
    set_departments = set(unique_departments)
    listed_dept = list(set_departments)
    listed_dept.sort()
    final_departments = []
    for department in listed_dept:
        item_count = 0
        for item in range(0, len(inventory)):
            if inventory[item]['department'] == department:
                item_count += 1
            else:
                pass
        final_departments.append({'department': department, 'item_count': item_count})
    print('________________________________')
    print('There are', len(final_departments), 'departments')
    print('________________________________')
    for items_to_print in range(0,len(final_departments)):
        if final_departments[items_to_print]['item_count'] > 1:
            print('+',final_departments[items_to_print]['department'].capitalize(), "(",final_departments[items_to_print]['item_count'], 'products)')
        else:
            print('+',final_departments[items_to_print]['department'].capitalize(), "(",final_departments[items_to_print]['item_count'], 'product)')

def combined(inventory):
    alpha_sorted_products(inventory)
    alpha_sorted_departments(inventory)

combined(products)