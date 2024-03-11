#!/usr/bin/python3
def print_last_digit(number):
<<<<<<< HEAD
if number < 0:
last_num = (-number % 10)
elif number >= 0:
last_num = number % 10
print("{:d}".format(last_num), end="")
return last_num
=======
    if number < 0:
        last_num = (-number % 10)
    elif number >= 0:
        last_num = number % 10
    print("{:d}".format(last_num), end="")
    return last_num
>>>>>>> 735813b46930c32943fce02180a9d2045d6839d2
