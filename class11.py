#If, else, elif

x = 5
if x > 5:
    print("X is greater than 5")
elif x == 5:
    print("X is equal to 5")#we can add more elif
else:
    print("X is less than 5")
print("out")

x_two = 15
y = 20

#And is a condition when 2 option must be valid to enter the if

if x > 10 and y > 25:
    print("X is greater than 10 and Y is greater than 25")

#Or is used when one of the conditions is valid
if x > 10 or y > 25:
    print("X is greater than 10 or Y is greater than 25")

#not is used to negate a condition
if not x>10:
    print("X is not greater than 10")

#If inside an if

is_member = True
age = 5

if is_member: #We don't add condition because it validates if it is true
    if age >= 15:
        print("You have access because you're a member and you're more or equal to 15 years old")
    else:
        print("You don't have access because you are less than 15 years old")
else:
    print("You are not a member and DON'T HAVE ACCESS")
