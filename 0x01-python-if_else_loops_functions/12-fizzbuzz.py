#!/usr/bin/python3
def fizzbuzz():
<<<<<<< HEAD
for i in range(1, 101):
if i % 3 == 0 and i % 5 == 0:
print("FizzBuzz ", end="")
elif i % 3 == 0:
print("Fizz ", end="")
elif i % 5 == 0:
print("Buzz ", end="")
else:
print("{:d} ".format(i), end="")
=======
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")
>>>>>>> 735813b46930c32943fce02180a9d2045d6839d2
