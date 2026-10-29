import random
import time
messages = ["spooky", "scary", "skeletons", "shivers", "spine"]
for i in range(9):
    try:
        rand = random.randint(0,5)
        print(messages[rand])
    except IndexError:
        print("ERROR: Something is trying to communicate...")
    finally:
        print("The computer is watching you.")
    time.sleep(1)