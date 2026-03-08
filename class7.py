name = input("ingrese su nombre: ")
print(name)
age = input("Ingrese su edad: ")
print(age)

#Using input always makes the variable a str (string)
print(type(name))
print(type(age))

#To convert the str a int we cast it this way:

age2 = int(input("Ingrese su edad: "))
print(type(age2))