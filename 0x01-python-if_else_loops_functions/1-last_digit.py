#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
last = abs(number % 10)
if number < 0:
    last = (last) % -10

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
=======

if number >= 0:
    l_digit = number % 10
else:
    l_digit = number % -10

print("Last digit of {} is {}".format(number, l_digit), end='')

if l_digit > 5:
    print(" and is greater than 5")
elif l_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
>>>>>>> refs/remotes/origin/main
