#!/usr/bin/python3
<<<<<<< HEAD
"""
Print the ASCII alphabet in lowercase, not followed by a new line.
"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
=======
for ch in range(97, 123):
     print("{:c}".format(ch), end='')
>>>>>>> refs/remotes/origin/main
