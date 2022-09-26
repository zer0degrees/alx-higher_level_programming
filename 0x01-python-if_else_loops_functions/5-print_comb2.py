#!/usr/bin/python3
<<<<<<< HEAD

for num in range(0, 100):
    if num == 99:
        print(num)
    else:
        print('{:02d},'.format(num), end=" ")
=======
for num in range(0, 100):
    if num != 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("{:02d}".format(num))
>>>>>>> refs/remotes/origin/main
