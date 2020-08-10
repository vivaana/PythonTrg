# 1) Write a program to check the temperature of a room.
# The requirements are simple:
# Prompt the user to enter the room temperature (it could be -100 to +100 including 0).
# Should the temperature of the room is below zero, shout out "It's freezing out here!".
# If the temperature is above zero, say "Ok, at least we aren't freezing".
# If the temperature is 0, say "Hmm, it's cold".
the_temperature = eval(input("please enter a temperature"))
if the_temperature <0:
    print("it is freezing in here")
if the_temperature == 0:
    print("hmm it is cold")
if the_temperature > 0:
    print("at least it isn't cold ")
# If the user enters any number over 100 or below 100 degrees, alert him saying
# "I refuse to work with people who wouldn't follow instructions:)" 5 marks
user_degrees = eval(input("please enter 100 degrees"))
if user_degrees == 100:
    print("your fine to work with me")
else:
    print("I refuse to work with people who wouldn't follow instructions:)")

# 2) Write a program to find out if the given number is a positive or negative or zero number. 5 marks
users_number = eval(input("please enter a number"))
if users_number == 0:
    print("it is a zero number")
elif users_number >0:
    print(users_number,"is a positive number")
else:
    print(users_number,"is a negative number")
# 3) Write a program to find out if the number is an even or odd number. 5 marks
users_number = eval(input("please enter a number\n"))
if users_number % 2 == 0:
    print("even")
else:
    print("odd")
# 4) Given a range of numbers from 0 to 29,  write a program as per the requirements mentioned below:
# - if the number is a multiple of 3, print "Fizz"
# - if the number is a multiple of 5, print "Buzz"
# - if the number is a multiple of 3 and multiple of 5, print "FizzBuzz"
# - if the number is neither of the above, print the number (10 marks)
my_numbers = range(1,30)
for numbers in my_numbers:

    if numbers %3 == 0 and numbers %5 == 0:
        print("Fizzbuzz")

    elif numbers % 3 == 0:
        print("fizz")

    elif numbers % 5 == 0:
        print("buzz")

    else:
        print(numbers)
# 5) My mum sent me to Pizza Hut to pick up a pizza.
# There were quite a few toppings to select from.
# I was told to keep a note of these toppings so when she calls me I need to tell her.
#
# Write a program with a list of toppings.
# Make sure you have at least 10 toppings in your pizza (use your imagination).
# After noting down the toppings, I'll usually wait for my mum's call.
# When I receive her call I'll run through the toppings list shouting
# "Topping one is _______", "Topping two is ______".
#
# Write a program depicting this requirement. 10 marks.

pizza_toppings = ["cheese","mushroom","onion","pepper","olive","tomato","corn","feta cheese","jalapeno","chili"]

print("mum's call time to tell the toppings")
for toppings in pizza_toppings:
    print(f"this is a ,{toppings} topping")