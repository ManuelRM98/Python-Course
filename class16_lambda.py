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