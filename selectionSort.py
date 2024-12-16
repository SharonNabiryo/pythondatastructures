def selectionSort(A):
    # Get the length of the array
    n = len(A)
    # Print the initial state of the array
    print(f"Initial Array: {A}\n")

    # Loop through the array in reverse order (from last element to the second element)
    for i in range(n-1, 0, -1):
        # Assume the first element is the largest in the unsorted portion
        max_index = 0
        # Initialize counters for comparisons and swaps for each iteration
        comparisons, swaps = 0, 0

        # Finding the maximum element in the unsorted portion
        for j in range(1, i + 1):
            # Count each comparison made between elements
            comparisons += 1
            # If the current element is greater than the current maximum, update max_index
            if (A[j] > A[max_index]):
                max_index = j
                
        # Only swap if the max_index is different from the current index i
        if max_index != i:
            
            # Swap the found maximum element with the last unsorted element        
            A[i], A[max_index] = A[max_index], A[i]
            # Increment the swap counter
            swaps += 1

            # Print the correct elements being swapped
            print(f"Swap {A[i]} and {A[max_index]}: {A}")
        else:
            # If no swap is needed, just print the current element remains in place
            print(f"No swap needed for {A[i]}: {A}")

        # Print the current state of the array after the swap
        print(f"Iteration {n-i}: Comparisons = {comparisons}, Swaps = {swaps}\n")

    # Return the sorted array with a message    
    return f"Sorted Array: {A}"
    



try:
    # Get input from the user as a string of numbers separated by spaces
    x = input("Enter an array of numbers sperated with spaces: ")
    # Check if user provided an input
    if x.strip():
        # Convert the input string into a list of integers
        A = list(map(int, x.split()))
        print("\nSorting user Array")
        # Call the selectionSort function and print the sorted result
        selectionSort(A)
    else:
        # If no input is provided, use predefined test cases
        A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
        A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
        A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

        # Print sorted list
        print("\nSorting A1")
        print(selectionSort(A1))
        print(f"---------------------------------------------------------------")
        print("\nSorting A2")
        print(selectionSort(A2))
        print(f"---------------------------------------------------------------")
        print("\nSorting A3")
        print(selectionSort(A3))
        print(f"---------------------------------------------------------------")
        
    
except ValueError:
    # Handle cases where the input is not a valid integer
    print("Invalid Input! Please enter integers only")



