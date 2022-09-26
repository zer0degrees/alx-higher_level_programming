#!/usr/bin/python3
<<<<<<< HEAD

for letter in range(ord('a'), ord('z') + 1):
    if letter != 113 and letter != 101:
        print('{}'.format(chr(letter)), end='')
=======
for ch in range(97, 123):
    if ch != 101 and ch != 113:
        print("{:c}".format(ch), end='')
>>>>>>> refs/remotes/origin/main
