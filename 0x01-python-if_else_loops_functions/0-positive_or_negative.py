#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
<<<<<<< HEAD
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")
=======
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))
>>>>>>> refs/remotes/origin/main
