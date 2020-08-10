animals = {"Cow","Chicken","Goat"}
for animal in animals:
    print(animal )
print("---now no Goat---")
animals.remove("Goat")
for animal_2 in animals:
    print(animal_2)
