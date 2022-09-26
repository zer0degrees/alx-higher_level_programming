#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    result = 0
    count = 1

    while count < len(argv):
        result += int(argv[count])
        count += 1
    print(result)
