# 1. Print the individual characters of a string "hello" using for loop. 2 marks
my_word = "Hello"
for hello in my_word:
    print(hello)
# 2. Print the individual characters of a string "hello" using for loop but all the letters must be printed as capitals. 3 marks
for hello in my_word:
    print(hello.upper())
# 3. Prompt the user to provide his/her name, print each of the letters using for loop, all lower case. 2 marks
your_name = input ("what is your name please \n")

users_name = your_name
for name in users_name:
        print(name.lower())
# 4. Print this sentence "i love python", capitalizing each of the first word.
# (Note: There is no for loops in this question, this is a simple string operation) 3 marks
pythn="i love python"
print(pythn.title())

# 5. Print the individual letters from this sentence "i love python" using for loop,
# make sure each of the first word is capitalized. 5 marks
print()
for name in pythn.title():
    print(name)
# 6. Create a list of your favourite friends, make sure you have at least 5 of them in that list.
# Using "for" loop, print them one by one with a message "Hello, how are you {friend_name}". 5 marks
my_friends = ["Timmona","Happo","Frogo","panpo","Jamplee"]
for friends in my_friends:
    print(f"Hello how are you { friends}")
# 7. Create a list of roll numbers from 1 to 25 using range function.
# Create a for loop printing each of them with a message "Roll number {number}" 5 mark
roll_numbers=range(1,26)
for roll_number in roll_numbers:
    print(f"Roll number: {roll_number}")
# 8. An ATM dispenses £5, £10, £20, £50 notes.
# Create a program using a for loop dispensing the note.
# When dispensing each of these notes, make sure you print a message to the user saying
# "Here's your {denomination}" 5 marks
money_to_withdraw=int(input("How much money do you want, please enter in multiples of 5?"))
print(f"you wanted to withdraw £{money_to_withdraw}")
notes=[50,20,10,5]
for i in notes:
    print(f"you will get {money_to_withdraw//i} £{i} notes")
    money_to_withdraw=money_to_withdraw%i



# 9. A circus charges different ticket prices depending on a person’s age.
# The ticket is free for a person under the age of 10, if they are between 11 and 16, the ticket is £5;
# and if they are above age 16, the ticket is £10. Write a program asking their age.
# Calculate the cost of the ticket and tell them how much it'll cost them. 10 marks. 10 Marks
your_age = int(input("How old are you?"))
if your_age <10:
    print("your ticket is free! Come in.")

if  11 < your_age < 16 :
    print("your ticket for £5")

if your_age >16:
    print("your ticket is for £10")