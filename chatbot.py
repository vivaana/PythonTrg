# ## Extension### #
# #8. Create a Chatbot with user's input (expected to ask the following three questions and print out answers all of them) 9 marks
# - 1st question: Ask the user his/her name
your_Name = input("What is your name ")
# - Capture the user's input in a variable and
# - Greet the user with his name "Nice to have you her Mr/Miss/Mrs {name}"
print("hello",your_Name)
# - 2nd question: Ask the user "How are you doing today, Mr/Miss/Mrs {name}"
How_are_you_doing = input("How are you doing ")
#  - Capture the user's input in a variable and ask a life goal question:
what_do_you_want_to_become_in_the_Future = input("tell me a life goal ")
# - print("Ok, Mr/Miss/Mrs {name}. What do you want to do in life?"
what_to_do_in_life=input("ok "+ your_Name+ " what do you want to do in life?")
# - 3rd question: Give the user "Good to know, Mr/Miss/Mrs {name}. I am a chatbot but I sincerely wish your life goal become true!"
print("good to know, ", your_Name,". I am a chatbot but I sincerely wish your lifegoal -'",what_do_you_want_to_become_in_the_Future,"' become true!")
# - Finally, print out a goodbye message:
print("byebye",your_Name)
# - print("Have a nice day, Mr/Miss/Mrs {name}. "
print("have a nice day", your_Name)