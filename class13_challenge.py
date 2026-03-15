#Create a generator to see the odd and even numbers


limit = int(input("Write a number: "))

#Odd numbers
print("Odd Numbers generator")
def my_generator_odd(limit):
    starting = 0
    while starting < limit:
        if starting % 2:
            odd_num = starting
            yield odd_num
        # else:
        #     even_num = starting
        #     yield even_num
        starting += 1

for num in my_generator_odd(limit):
    print(num)

#Even numbers
print("Even Numbers generator")
def my_generator_even(limit):
    starting = 0
    while starting < limit:
        if not starting % 2:
            even_num = starting
            yield even_num

        starting += 1

for num in my_generator_even(limit):
    print(num)