menu = {
    1: 'tomatoes',
    2: 'onions', 
    3: "paprika's", 
    4: 'ham', 
    5: 'cheese', 
    6: 'salami', 
    7: 'chicken', 
    8: 'bacon'
}

prices = {
    1: 1.20,
    2: 0.90,
    3: 0.75,
    4: 2.10,
    5: 1.45,
    6: 0.90,
    7: 1.20,
    8: 1.30
}

order = []
price = []
ordering = True

print(F"Available pizzatoppings: \n{menu}\n")
print("Enter the respective number of your preferred topping to add to your order")
print("Enter '9' to finish your order\n")

while ordering:
    pizza_toppings = int(input("Add topping number: "))
    if pizza_toppings == 9:
        ordering = False
        break
    for item in menu.keys():
        if pizza_toppings == item:
            order.append(menu[pizza_toppings])
            price.append(prices[pizza_toppings])

print(F"Ordered toppings: {order}")
sum_price = sum(price)
print(F"Price toppings: {sum_price} euro")


    






















