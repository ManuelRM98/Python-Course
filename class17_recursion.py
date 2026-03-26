#factorial: using 5! = 5*4*3*2*1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_5 = print(factorial(5))

#fibonacci: sum numbers from 0 and 1: 0+1=1 1+1=2 1+2=3 2+3=5... === 0 1 1 2 3 5 8...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = 5
print(fibonacci(number))

#Challenge

#Calculate the sum of natural numbers: 4 = 4+3+2+1

def natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + natural_numbers(n-1)
    
number = 4
print(natural_numbers(number))