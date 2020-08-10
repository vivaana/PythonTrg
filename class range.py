num = range(0,51,2)
for numbers in num:
    print(numbers)





    ##FizzBuzz

num = range(1,16)

for numbers in num:


    if numbers %5==0 and numbers %3==0:
        print("FizzBuzz")

    elif numbers %3==0:
        print("Fizz")

    elif numbers %5==0:
        print("Buzz")

    else:
        print(numbers)


#################squares###################

square = []
for num in range(1,14):
    num**=3
    square.append(num)
print(square)

from turtle import *
for num in range(1,10000000000, 2):
    circle(num)
    done
