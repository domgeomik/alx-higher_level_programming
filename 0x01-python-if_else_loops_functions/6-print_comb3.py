#!/usr/bin/python3
for i in range(9):
<<<<<<< HEAD
for j in range(i + 1, 10):
if i * 10 + j < 89:
print("{:d}{:d}".format(i, j), end=", ")
=======
    for j in range(i + 1, 10):
        if i * 10 + j < 89:
            print("{:d}{:d}".format(i, j), end=", ")
>>>>>>> 735813b46930c32943fce02180a9d2045d6839d2
print("{:d}".format(89))
