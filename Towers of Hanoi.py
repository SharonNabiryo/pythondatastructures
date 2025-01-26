# SHARON NALUMU NABIRYO

def hanoi(n):
    if (n == 0):
        return 0
    else:
        return 2 * hanoi(n-1) + 1

while True:
    user_input = input("Enter the number of disks (or type 'exit' to quit): ").strip().lower()
    if user_input == 'exit':
        print("Goodbye!")
        break
    if user_input.isdigit():  # Check if the input is a valid non-negative number
        n = int(user_input)
        print(f"With {n} disks, you need {hanoi(n)} movements.")
    else:
        print("Please enter a valid non-negative number or 'exit' to quit.")
