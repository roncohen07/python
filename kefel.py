import sys

def generate_multiplication_table(user_input):
    if 1 <= user_input <= 10:
        for i in range(1, 11):
            result = user_input * i
            print(f"{user_input} x {i} = {result}")
    else:
        print("Please enter a number from 1 to 10.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            user_input = int(sys.argv[1])
            generate_multiplication_table(user_input)
        except ValueError:
            print("Please provide a valid number.")
    else:
        print("Usage: python kefel.py <number>")
