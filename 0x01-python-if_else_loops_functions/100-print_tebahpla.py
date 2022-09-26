#!/usr/bin/python3
<<<<<<< HEAD
for i in range(122, 96, -1):
    if (i % 2 != 0):
        print('{}'.format(chr(i - 32)), end='')
    else:
        print('{}'.format(chr(i)), end='')
=======
for ch in reversed(range(97, 123)):
    print("{:c}".format(ch if (ch % 2 == 0) else (ch - 32)), end='')
>>>>>>> refs/remotes/origin/main
