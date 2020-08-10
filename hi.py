

hi = "hi"
while hi != "no":
    hello = input("whats your name")
    print(f"{hi},{hello}")

    if hello == "no":
        print("i quit")
        break


import random
hi = random.randrange(1,130)
print(hi)