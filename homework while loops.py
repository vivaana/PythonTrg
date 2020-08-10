# 1. The initial value of room temperature is 0 degrees.
# Write a program to print the temperature of the room for every degree increase.
# When the temerature reaches 24 degress, print the message
# "It's hot, shutting down" message and exits. 5 marks
room_temperature = 0
room_temperature_ck = True
degrees = 24
while room_temperature_ck :
    print(room_temperature)
    room_temperature = room_temperature + 1
    if room_temperature == degrees:

        print("it is very hot, shutting down")
        room_temperature_ck=False

# 2. A movie cinema sells 79 tickets per show.
# Print a message "Issued a ticket  {ticket_number} " for every purchase.
# When the show is house full, print "House full, no more tickets available".
# Hint, use "while" loops 5 marks
movie_tickets = 79
while movie_tickets != 0:
    print(f"you have been issued Ticket :{movie_tickets}")
    movie_tickets = movie_tickets - 1
else:
    print("House full, no more tickets available")
# 3. Write a program to print integers from 0 till 100 using while loop.
# Make sure you use range function for fetching the integers. 5 marks
the_range = 0
while the_range in range(0,101):
    print(the_range)
    the_range=the_range+1
# 4. A variable "visitor_counter" keeps a tracks of website visitors.
# The initial value of the counter is 0.
# Write a program using while loop to print out the visitor number for each time a vistor visits the site.
# If the visitors are over 100, exit the while loop and print
# "System overloaded, exiting" message to the console. 5 marks
visitor_counter = 0
while visitor_counter in range(0,101):
    print(f"This is website visitor {visitor_counter}")
    visitor_counter = visitor_counter + 1
else:
    print("System overloaded, exciting")

# 5. A receptionist chatbot at a dental practice asks for each of the patient's name as they enter the practice.
# The chat bot stops asking when it receives a "quit" word. Your job is to assist in writing a receptionist chatbot program. (Hints: use while loop; see if you need to ask user input in the while loop too) 5 marks
print("I am a receptionist's chat bot and I will keep asking for your name unless you enter quit. ")
your_name = "w"
while your_name != "quit":
    your_name = input("what is your name")

# 6. Write a loop that prompts the user to enter a series of numbers to guess a number game
# (guessing the number isn't the point of program here, remember).
# The loop ends once they say 0 value. Print out the the numbers as they guess.
# Print out "I give up once the program receives 0 and exits. 5 marks
your_numbers = 1
print("I give up once the program receives 0 and exits.")
while your_numbers != 0:
    your_numbers = eval(input("please enter a number."))

else:
    print("I give up, you typed 0")
