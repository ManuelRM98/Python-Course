#For Cycle

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:#values of list will be saved in i
    print("Here i is equal to:",i+1)

#We can iterate based on a data collection giving a starting point and an end
#Using range

for i in range(10): #numbers from 0 to 9
    print(i)

#We can specify the starting point with a ,

for i in range(3,10): #numbers from 3 to 9
    print(i)

fruits = ["Apple", "Pear", "Grape", "Orange", "Tomato"]
for fruit in fruits:
    print(fruit)
    if fruit == "Orange":
        print("Orange found")


#While: We can iterate other collections when it is subject of a conditional

x = 0

while x < 5:
    print("x is equal to:",x) 
    x += 1

#There are cases that I need to find a specific data. Break.

y = 0

while y < 5:
    if y == 3:
        break
    print(y) 
    y += 1

#There are cases where I won't finish the code, but I want to skip a step of the code. Continue

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:#values of list will be saved in i
    if i == 3:
        continue #Doesn't run the number 3
    print("Here i is equal to:",i)

    numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
	print(f"i is equal to: {i}")