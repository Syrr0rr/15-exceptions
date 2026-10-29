'''
Exeptions: What is thrown when an error in you application occurs.
Crashes your program.

print(4/0)
ZeroDivisionError: division by zero

str = "Cheese"
if str > 1:
    print(5)
TypeError: '>' not supported between instances of 'str' and 'int'

print(int("A"))
ValueError: invalid literal for int() with base 10: 'A'

Try: The code block that is potentially dangerous
Exept: The code to run if an exeption occurs
Finall: The block of code that runs after a try/exept either way 


'''
# try:
#     num1 = int(input("First num: "))
#     num2 = int(input("Second num: "))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Cant divide by zero")
# except ValueError:
#     print("Please enter vad integer")


# try:
#     num1 = int(input("First num: "))
#     num2 = int(input("Second num: "))
#     print(num1/num2)
# except ZeroDivisionError, ValueError:
#     print("Errorrrrrrr")

file = open("somefile.txt", "w")



try:
    num1 = int(input("First num: "))
    num2 = int(input("Second num: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Errorrrrrrr")
except ValueError:
    print("Please enter valid int")
finally:
    print("Operation complete")