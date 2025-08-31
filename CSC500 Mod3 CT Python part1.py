item_name1 = input('Enter food item name:\n')
item_price1 = float(input('Enter price:\n'))
item_quantity1 = int(input('Enter quantity:\n'))

item_name2 = input('Enter food item name:\n')
item_price2 = float(input('Enter price:\n'))
item_quantity2 = int(input('Enter quantity:\n'))

drink_name = input('Enter drink name:\n')
drink_price = float(input('Enter drink price:\n'))
drink_quantity = int(input('Enter quantity:\n'))

item1_cost = item_price1 * item_quantity1
item2_cost = item_price2 * item_quantity2
drink_cost = drink_price * drink_quantity

subtotal = item1_cost + item2_cost + drink_cost
gratuity = subtotal * 0.18
tax = subtotal * 0.07
total_cost = subtotal + gratuity + tax

print()
print('RECEIPT\n')
print(f'{item_name1} - {item_quantity1}: {item_price1}')
print(f'{item_name2} - {item_quantity2}: {item_price2}')
print(f'{drink_name} - {drink_quantity}: {drink_price}\n')

print(f'Subtotal: ${subtotal:.2f}')
print(f'Gratuity (18%): ${gratuity:.2f}')
print(f'7% Sales Tax: ${tax:.2f}')
print(f'TOTAL: ${total_cost:.2f}')

      

