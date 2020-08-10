# These are the two numbers

number1 = 10
number2 = 20

sum_of_numbers = number1 + number2
print("Sum of numbers is ", sum_of_numbers)

your_Number1= eval(input("please choose first number"))
your_Number2 = eval(input("please choose second number"))

# 1. Find out product of two numbers and print out
def MultiplyNumers(no1,no2):
    print("the product of your numbers is",no1*no2)
# 2. Find out division of two numbers and print out
def divideNumbers(no1,no2):
    print("the product of your numbers is",no1/no2)
# 3. Find out subtraction of two numbers and print out
def subtractNumbers(no1,no2):
    print("the product of your numbers is",no1-no2)


MultiplyNumers(your_Number1,your_Number2)
divideNumbers(your_Number1,your_Number2)
subtractNumbers(your_Number1,your_Number2)