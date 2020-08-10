# OPEN function will take two inputs:
# A name of the file, MODE -> r -> reading, w-> writing, x -> creating
name = input("What is your name?")
opening = open("friends.txt","r")
# name = input("What's your name?")
# tanya = open("friends.txt","r")

# print(tanya.read())
print(opening.read())
count = 1
# count = 1
for names in opening:
    print(count)
    count += 1
    print(names)
# for name in tanya:
#     print(count)
#     count += 1
#     print(name)
#
#
# Write a program to fetch a list of animals from
# animals.txt file