
def tribo(n, values):
    if ((n-1) < len(values)):
        return values[n - 1]
    ans = (tribo(n-1, values) + tribo(n-2, values) + tribo(n-3, values))
    values.append(ans)
    return ans

def main():
    while True:
        userInput = input("Enter a positive integer (or type 'exit'to quit): ")
        if userInput.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            n = int(userInput)

            if n <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            
            values = [1, 1, 1]
            print("Initial values:", values)
            result = tribo(n, values) 
            print(f"The element in position {n} of the Tribonacci sequence is {result}.")
            print("Updated values:", values)
                
        except ValueError:
            print("Invalid input. Please enter a valid positive integer or 'exit' to quit.")
        
main()
