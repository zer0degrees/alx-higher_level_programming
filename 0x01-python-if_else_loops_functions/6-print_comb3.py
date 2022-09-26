#!/usr/bin/python3
<<<<<<< HEAD

for num in range(0, 9):
    for num_1 in range(1, 10):
        if num < num_1:
            if num == 8:
                print("{}{}".format(num, num_1))
            else:
                print("{}{},".format(num, num_1), end=" ")
=======
for num in range(0, 90):
    if num % 10 > num / 10:
        if num != 89:
            print("{:02d}, ".format(num), end='')
        else:
            print("{:02d}".format(num))
>>>>>>> refs/remotes/origin/main
