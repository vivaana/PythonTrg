# ## Create the programs in PyCharm and execute them. Once ran successfully, attach the source code  in a text or doc format to your assignment.
# ## Full marks will be awarded for those who write simple programs with readable comments and descriptive variable names.
# ## The idea is to test you the concept of f-strings. So please use the f-strings in your program
# ## Q 4 is an extension, please try to do it if you can.
# - Make sure you use f-strings (if needed, read the f-strings class notes)
# #1 Create a program with one variable for representing a country. Ask the user the capital city of this country. Capture the user's response and print out to the console something along the lines of this: "The capital city of {country} is {user_response} (3 Marks)

# #2 Create a program with one variable representing the temperature in c. Convert the temp in F to Celcius. Print both Fahrenheit and Celcius temperatures
# - Make sure you use f-strings to print out the values of both F and C. (5 Marks)
temp_celcius=23
temp_fahrenheit=temp_celcius*(9/5) + 32
print(F"The temp in celcius is {temp_celcius} and in fahrenheit is {temp_fahrenheit}")
# #3 Re-create the same problem mentioned in #2 except this time ask the user to input the Fahrenheit. For example, "Hello, please enter the current temp in Fahrenheit".  Convert the temp in F to Celcius. Print both Fahrenheit and Celcius temperatures as f-string like : "Temperature of {f} is {c}"  (7 Marks)
# - Ask the user to input the temp in Fahrenheit (create appropriate type)
# - Use the formula to convert it into Celcius
# - Make sure you use f-strings to print out the values of both F and C.
# - The formula for converting the temp from Fahrenheit to Celcius is: Temp in C = (Temp in F - 32) * 5/9
users_fahrenheit = eval(input("please enter the temperature in fahrenheit: "))
temp_celcius = (users_fahrenheit - 32) * 5/9
print(F"The temperature is {users_fahrenheit} and in celsius {temp_celcius}")
# #4 Extension 10 Marks
# # Create a program asking the user to enter the temperature in Celcius. This time convert the temperature into Fahrenheit and output the values of both temperatures using f-strings like : "Temperature of {f} is {c}". You need to find out the formula for conversion from Celcius to Fahrenheit (remember the above formula, reduce your celcius-to-fahrenheit formula from that)
users_celsius = eval(input("please enter the temperature in celcius: "))
temp_fahrenheit_2 = users_celsius * (9/5)+ 32
print(F"the temperature in fahrenheit is {temp_fahrenheit_2} and in celsius it is {users_celsius}")