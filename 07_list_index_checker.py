animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"]
try:
    i = int(input("index:"))
    print(animals[i])
except IndexError:
    print("That is not in the list!")
