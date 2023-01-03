def most_expensive(price_list):
  """
  Iterate through a list and find the most expensive item
  """
#Set up the variable
max_price = 0
max_price_item = ""
#iterte, unpacking the tuple
for description,price in price_list:
# If this is the maximum price, record that in our variable	
  if price > max_price:
    max_price = price
    max_price_item = description
# if it is not the maximum price, do nothing
  else:
     pass
# return the maximum price item and its price
return max_price_item, max_price

#provide the data

price_list = [("Pineapple", .5),("pears", .7),("orange", .9)]
# call the function and unpack its return values
product, price = most_expensive(price_list)
print(product, price)
  