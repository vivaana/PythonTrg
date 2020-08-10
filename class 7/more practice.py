# 1) Write a loop using "while" loop asking user for a random name.
# Quit the program if the random string is "q" or "quite" or "end" or "bye" or empty string.
# Also make sure the input can be of any case
# (user can input Q or q or Quit or qUiT - so make sure your program takes care of it.
# (hint: try using "break" statement!) 5 marks
name=input("Enter name")
while name != "q"or"quit"or"end"or"bye":
    name=input("Enter name")
    name=name.lower()

    if name == "q":
        break

    elif name == "quit":
        break

    elif name == "end":
        break

    elif name == "bye":
        break
# if name = "q" or name = "q"

# 2. Create a program that reads the individual characters of a single-word string.
# If any of the character is "q" the program must quit.
# For example, "hello" will print all the characters but "queen" will not run. (hint: use for loop). 5 marks
word = input("give me a word")
for letters in word:

    if letters == "q":
        break

    else:
        print(letters)

# 3. Write a for loop printing even numbers from 1 to 10 using "range" function
# (hint you can do with out range,
# but the question here is asking superficially using range function - note that) 5 marks
odd_or_even = eval(input("please enter a numbers up to 10\n"))
for numbers in odd_or_even:
    print(numbers,"is",numbers % 2 == 0)
# 4. Using a for loop, can you write a program to print values 5, 4, 3, 2,1,0.
odd_or_even = eval(input("please enter 5,4,3,2,1,0 \n"))
for numbers in odd_or_even:
    print(numbers,"is",numbers % 2 == 0)
# 5. Prompt a user to provide his/her age.
# If the age is below 13, print out "You are pre-teen".
# If the age is equal to or above 13, print out
# "You are a teenager" (we've done this program in the earlier exercises, so it should be relatively easy) 5 marks

age = eval(input("what is your age?"))

if age <13:
    print("you are pre-teen")

else:
    print("You are a teenager "+"we've done this program in the earlier exercises, so it should be relatively easy")