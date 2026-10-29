prices = {"pizza": 12, "burger": 8, "fries": 4, "soda": 2}
try:
    item = input("Item: ")
    print(prices[item])
except KeyError:
    print("That item doesnt exist")