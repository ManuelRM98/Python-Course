#To create a list use [], to separe the data use ','

to_do = ["go to hotel", "Lunch time", "Go to museum", "Go back to the hotel"]
print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers))

mix = ["one", 2, 3.14, True, [1, 2, 3]]
print(mix)

#We can check the number of data saved

print(len(mix))

#To check a specific value in a list

print("first element:", mix[0]) 
print("last element:", mix[-1])

#We can also check individual elements of a string variable

string = "Hello World"
print("first element:", string[0]) 
print("last element:", string[-1])

#There's another option to check specific values for a list

print(mix[0:2])

#Adding values to a list (adds the value at the end of the list)

mix.append(False)
print(mix)

#Adding values in a specific position of the list

mix.insert(1,"a")
print(mix)

#To consult the position of an element in the list

print(mix.index("a"))

#To check the maximum and minor

other_numbers = [1,2,100,90.45,3,4,5]
print(other_numbers)
print("Max:",max(other_numbers))
print("Min:",min(other_numbers))

#To remove an element of the list

del other_numbers[-1]
print(other_numbers)

#To remove multiple elements of the list

del other_numbers[:2]
#removing position 0 and 1
print(other_numbers)

#To remove all the elements of the list

del other_numbers
#print(other_numbers)

#To copy a list to a new list

a = [1,2,3,4,5]
b = a
print(b)

#The problem is that whenever you modify a, b will also be modified because they use the same memory space

del a[0]
print(a)
print(b)
print(id(a))
print(id(b))
c = a[:] #copy all the elements
print(id(c))

a.append(6)
print(a)
print(c)