add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,5))

#applying lambda with lists

#Square of each number (range from 0 to 10)
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Square of numbers:",squared_numbers)

#Obtaining pair numbers
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Even numbers:",even_numbers)

#Real life example

#Imagine your API returns a list of product prices in cents, 
# and you need to convert them to dollars before sending the response to the frontend:

prices_in_cents = [1999, 4999, 14999, 999, 29999]

# Convert every price from cents to dollars, rounded to 2 decimals
prices_in_dollars = list(map(lambda price: round(price / 100, 2), prices_in_cents))

print(prices_in_dollars)
# [19.99, 49.99, 149.99, 9.99, 299.99]