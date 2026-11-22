def shopping_list(cart, *items):
    for item in items:
        cart.append(item)
    return cart

cart = []

cart = shopping_list(cart, "apples")
cart = shopping_list(cart, "bread", "milk", "eggs", "butter")
cart = shopping_list(cart, 'ink', 'backpack', 'pens', 'notebook')

print("Items in the cart: ", cart)