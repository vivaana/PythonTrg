# 29 May (Edited 29 May)
# # Write the following programs in your PyCharm IDE, execute them. If they ran successfully, attach the code to your assignment as a text file or a document. The last one is an extension for 9 marks. Try if you can.
#
# # Do note I'll provide full marks for readable code with comments and descriptive variable naming and best practices. Don't hesitate to ping me if you are stuck or need help.
#
#
# # 1. Write a program asking the user to input the user's name. Print the name and type of the variable to the console 1 mark
yourName = input("What is your name?")
print(yourName)
print(type(yourName))
# # 2. Write a program asking the user to input their weight. Print the name and type of the variable to the console 1 mark
yourWeight = eval(input("What is your weight     "))
print(yourWeight)
print(type(yourWeight ))
# # 3. Write a program asking the user to input their age. Age is entered as a whole number. Print the name and type of the variable to the console 1 mark
How_old_are_you = int(eval(input("How old are you")))
print(How_old_are_you)
print(type(How_old_are_you))
# # 4. Write a program asking the user to input their age. Age is entered as a whole number (ignore leap years).  2 marks
# - Now print the age in months. For example, "You are xxx months old"
# - Print the age in days. For example: "You are xxxxx days old"
# Clue: make sure you work on an appropriate type (str type won't allow mathematical operations, remember that)
#
# # 5. Write a program to calculate area of a circle given a radius 3 marks
# - Ask the user to input the radius of a circle.
# - Once the radius is captured, calculate the area of the circle and
# - Output the answer to the user.
aRadius = eval(input("Please give me a radius?  "))
#aRadius = int(aRadius)
PI = 3.14
area =aRadius ** 2 * PI
print("your answer is " + str(area))


# # 6. Write a program to calculate area of a square given the length of a side 3 marks
# - Ask the user to input the radius side/length of a square
# - Once the side is captured, calculate the area of the square and
# - Output the answer to the user.
Square_area = eval(input("please give me a length of a side of a Square? "))
area = Square_area ** 2
print("your area of the square is",area)
# # 7. Write a program to calculate area of a rectangle given its length and width. 5 marks
# - Ask the user to input the length of the rectangle
userLength = eval(input("please give me a length of the rectangle "))
# - Capture the length in a variable
# - Ask the user to input the width of the rectangle
userwidth = eval(input("please give me a width of the rectangle "))
# - Capture the width in a variable
# - Once the both length and width are captured, calculate the area of the rectangle and
# - Output the answer to the user.

print("your answer is ",userLength * userwidth)
