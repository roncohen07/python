# kefel.py
import sys

try:
    # Python 2
    input_func = raw_input
except NameError:
    # Python 3
    input_func = input

try:
    user_input = int(input_func("Enter a number from 1 to 10: "))
except ValueError:
    print("Please enter a valid number.")
    sys.exit(1)

if 1 <= user_input <= 10:
    for i in range(1, 11):
        result = user_input * i
        print(f"{user_input} x {i} = {result}")
else:
    print("Please enter a number from 1 to 10.")
