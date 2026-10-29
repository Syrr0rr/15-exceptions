
try:
    num1 = int(input("First num:"))
    num2 = int(input("Second num:"))
    print(num1/num2)
except ZeroDivisionError:
    print("Cant divide by zero bub")
