import sys

if len(sys.argv) != 2:
    print("Please provide a number from 1 to 10 as a command-line argument.")
    sys.exit(1)

user_input = int(sys.argv[1])

if 1 <= user_input <= 10:
    for i in range(1, 11):
        result = user_input * i
        print(f"{user_input} x {i} = {result}")
else:
    print("Please enter a number from 1 to 10.")
