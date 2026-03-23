def greet():
    print("Hello World")

greet()

def greet2(name, last_name):
    print("Hello",name, last_name)

#Function is expecting to recieve an information, in this case you have to use something inside () 
greet2("Manuel", "Rodriguez")
greet2("Mateo", "Ramirez")

#We can add an = to the variable to make some value by default if the parameter it gets is empty
def greet3(name, last_name="Don't have last name"): 
    print("Hello",name, last_name)

greet3("Valentina")

#We can use another order for the parameters
greet3(last_name="Madrid", name="Camilo")

#Calculator example

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def calculator():
    while True:
        print("Select an operator")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        option = input("Select the option (1,2,3,4,5): ")

        if option == "5":
            print("Exiting the calculator")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Write the first number: "))
            num2 = float(input("Write the second number: "))

            if option == "1":
                print("The operation 'sum' was done:", add(num1,num2))
            elif option == "2":
                print("The operation 'substract' was done:", substract(num1,num2))
            elif option == "3":
                print("The operation 'multiply' was done:", multiply(num1,num2))
            else:
                print("The operation 'divide' was done:", division(num1,num2))

        else:
            print("Option incorrect, please try again")

calculator()
