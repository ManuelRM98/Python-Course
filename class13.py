#Iterators

#Creating a list

my_list = [1, 2, 3, 4]

#Obtain the iterator
my_iter = iter(my_list)

#use the iterator
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#If use use another one, it will throw an error due to the number not existing

#Using chains or strings to use iter

#Creating the Chain
text = "Hello World"

#Creating the iterator
iter_text = iter(text)

#Chain interation

for chain in iter_text:
    print(chain)

#Iteration creation for odd numbers

#Limit

limit = 10
#Creating the iterator using range
odd_iter = iter(range(1, limit+1,2))

#using the iterator
for num in odd_iter:
    print(num)

#GENERATORS

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


#FIBONACCI - numbers that are increasing its value with a sum with the previous one
# 0 1 1 2 3 5 8 13 21

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

for num in fibonacci(10):
    print(num)