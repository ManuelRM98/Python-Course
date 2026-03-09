matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
#even though you can see the print in a line, it respects the rows and columns
print(matrix[2][1])

#tuple: are immutables, that means once they're created they cannot be modified

numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
numbers[0] = 'ones'
print(numbers)

#we can also create a tuple without ()
#numbers = 1,2,3,4,5