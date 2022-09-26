#!/usr/bin/python3
<<<<<<< HEAD

# print_last_digit: function that print last digit of any number
# Number: arguments that hold pass variable or value
# last: hold last digit of passed argument
# Return: Last digit

def print_last_digit(number):
    if number < 0:
        last = (-1 * number) % 10

    else:
        last = number % 10

    print('{}'.format(last), end='')

    return last
=======
def print_last_digit(number):
    if number >= 0:
        l_digit = number % 10
    else:
        l_digit = number % -10
        l_digit *= -1

    print("{:d}".format(l_digit), end='')
    return (l_digit)
>>>>>>> refs/remotes/origin/main
