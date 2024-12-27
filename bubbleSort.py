def bubbleSort(A):
    # Get the length of the array
    n = len(A)
    
    # Print the initial array
    print(f"Initial array: {A}\n")

    # Outer loop for each pass through the array
    for i in range(n - 1):
        print(f"Iteration {i + 1}: {A}")
        swapped = False
        comparisons, swaps = 0, 0  # Counters for each iteration

        # Inner loop to compare adjacent elements
        for j in range(n - i - 1):
            comparisons += 1  # Increment comparisons counter
            if A[j] > A[j + 1]:
                
                # Swap the elements if they are in the wrong order
                print(f"Swap {A[j]} and {A[j + 1]}: ", end="")
                A[j], A[j + 1] = A[j + 1], A[j] # Perform the swap
                swaps += 1 # Increment swaps counter
                swapped = True
                print(A)  # Print the array after each swap
        
        # Print the summary for the current outer loop iteration
        print(f"Comparisons = {comparisons}, Swaps = {swaps}\n")
        
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
    
    # Print the final sorted array
    print(f"\nSorted array: {A}")
    print("-------------------------------------------------------------")

#ask for user input
try:
    x = input("Enter an array of numbers seperated by spaces: ")

    # check if user entered something         
    if x.strip():
            A = list(map(int, x.split()))
            print("\nSorting user Array")
            bubbleSort(A) # Sort the user's array
    else:
        # If no input is provided, use predefined arrays for testing
        A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
        A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
        A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]


        # Testing the algorithm
        print("\nSorting A4:")
        bubbleSort(A4)
        print("\nSorting A5:")
        bubbleSort(A5)
        print("\nSorting A6:")
        bubbleSort(A6)

# Handle cases where the input cannot be converted to integers
except ValueError:
    print("Invalid Input! Please enter integers only")
