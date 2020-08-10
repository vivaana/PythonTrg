import random

# 1 Print the output from the following statement. 2Marks
#
# python = "I love Python. My mon hates Python and probably get a heart attack if she sees one. My dad kills a Python if he sees one"
##############################This is my attempt but i am stuck################################
print("I love Python. My mum hates Python and probably get a heart attack if she sees one. My dad kills a Python if he sees one")
# python_type = bool(python)
# print(python_type)
#
# 2. What is the output for all the following statements. Please don't copy them to PyCharm and execute them to find the answers - it's cheating :) Look at the question carefully and deduce the answer. I'll be really happy if you find the answer by thinking and deducing than coding! This is not a coding question. 20 Marks
#print(bool("[]"))
"True"
#print(bool(1*2))
"True"
#print(bool(-1))
"True"
#print(bool())
"False"
#print(bool("0.0"))
"True"
#print(bool("0"))
"True"
#print(bool(""))
"False"
#print(bool("false"))
"True"
#print(bool("False"))
"True"
#print(bool("true"))
"True"
# print(bool("False"))
"True"
# print(bool("--"))
"True"
# print(bool(True))
"True"
# print(bool(False))
"False"
# print(bool(0))
"False"
#print(bool(0.0))
"False"
# print(bool(-1))
"True"
#print(bool(-0))
"False"
#  print(bool(int("12")))
"True"
#print(bool(str(12)))
"True"
# 3. What is the output of this:
# It seems tomorrow is not a sunny day, according the Dimpy the weather forecaster.
# But your job is to ask her the weather for tomorrow.
# Write a program asking Dimpy what is the weather like tomorrow.
weather_types = ["sunny","windy","snowing","pleasant","thunderstorms","rain","cloudy"]
tomorrow_weather = input("Hello I am Dimpy, do you want the latest weather report for tomorrow, please answer only Y for yes or N for no ")

Dimpy_weather = random.choice(weather_types)

if tomorrow_weather == "Y":
    print("tomorrows weather is",Dimpy_weather,", have a nice day!")

    if Dimpy_weather == "sunny" or Dimpy_weather == "windy" or Dimpy_weather == "pleasant" or Dimpy_weather == "cloudy":
        print("Hello family tomorrow weather is",Dimpy_weather,", lets go for an outing")

    else:
        print("Hello family tomorrow weather is", Dimpy_weather, ", I think that you shouldn't go out Tomorrow")

else:
    print("You didn't want the latest weather report per your selection, Ok bye have a good day")

    # Based on her answer, can you write a bool variable with an "if" statement to let your family know
    # if the family can go out to an outing or stay put? 8 Marks
