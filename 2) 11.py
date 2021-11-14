# Python Program to Check Number is Divisible by 8 and 12

number = int(input(" Please Enter any Positive Integer : "))

if((number % 8 == 0) and (number % 12 == 0)):
    print("Given Number {0} is Divisible by 8 and 12".format(number))
else:
    print("Given Number {0} is Not Divisible by 8 and 12".format(number))
