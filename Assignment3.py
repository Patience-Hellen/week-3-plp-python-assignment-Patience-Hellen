def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discounted_price = price - (price * discount_percent/100)
    return discounted_price
  else:
    return price

price = float(input("Give the price of the item: "))
dicount_percent = float(input("Give the discount percentage: "))

print(calculate_discount(price, discount_percent))
