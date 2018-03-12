"""Isaac"""
while True:
    name = str(input("What is your name: "))

    if name.alpha():
        print("Your name is {}".format(name))
        break
    else: name = str(input("What is your name: "))
