#Enter the item
item = input("Enter the item: ")

#Enter the price
price = input("Enter the price")

item_length = len(item)
price_length = len(price)

total_length = 25

remaining_length = total_length - (item_length + price_length)



space_string = "." * remaining_length

price_list = item + space_string + price
print(price_list)