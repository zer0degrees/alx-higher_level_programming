#!/usr/bin/python3
def uppercase(str):
<<<<<<< HEAD
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(i) - (ord('a') - ord('A')))
        print("{:s}".format(i), end='')
=======
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[i]) - num), end='')
>>>>>>> refs/remotes/origin/main
    print()
