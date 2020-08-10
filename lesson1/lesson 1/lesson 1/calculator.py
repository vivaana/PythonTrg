# calculator.py

#number1 = 94
#number2 = 108
#print(number1 + number2)


number1 = 5
number2 = 5
print(number1*number2)

choice_no1=eval(input("Please enter the first number \n"))
choice_no2=eval(input("Please enter the second number \n"))

# 1. Find out product of two numbers and print out
def product_numbers(no1,no2):
    print("The product of the number ", no1,"and",no2,"is:",no1*no2)
# 2. Find out division of two numbers and print out
def division_numbers(no1,no2):
    print("The division of the number ", no1,"and",no2,"is:",no1/no2)
# 3. Find out subtraction of two numbers and print out
def subtraction_numbers(no1,no2):
    print("The subtraction of the number ", no1,"and",no2,"is:",no1-no2)

product_numbers(choice_no1,choice_no2)
division_numbers(choice_no1,choice_no2)
subtraction_numbers(choice_no1,choice_no2)