#!/usr/bin/python3
def uppercase(str):
<<<<<<< HEAD
for i in str:
if ord("a") <= ord(i) <= ord("z"):
i = chr(ord(i) - 32)
print("{:s}".format(i), end="")
print()

=======
    for i in str:
        if ord("a") <= ord(i) <= ord("z"):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
>>>>>>> 735813b46930c32943fce02180a9d2045d6839d2
