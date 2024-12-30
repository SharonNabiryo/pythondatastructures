def Min(A, start, end):
    # Print the start and end indices with their slice at the beginning of each call
    print(f"Checking A[{start}:{end}] -> {A[start:end+1]}")
    print(f"Start Value: {A[start]}, End Value: {A[end]}\n")
    
    # Base case: If the subarray has only one element
    if start == end:
        return start  # Return the index instead of the value

    # Divide the array into two halves
    mid = (end + start) // 2
    fst_index = Min(A, start, mid)
    lst_index = Min(A, mid + 1, end)
    
    # Find the minimum between the two halves by comparing their values
    result_index = fst_index if A[fst_index] < A[lst_index] else lst_index
    print(f"Minimum in A[{start}:{end}] is {A[result_index]}\n")
    return result_index

try:
    x = input("Enter an array of numbers separated by spaces: ")
    
    if x.strip():
        A = list(map(int, x.split()))
        start = 0
        end = len(A) - 1

        # Get the index of the minimum element
        min_index = Min(A, start, end)
        print(f"\nThe minimum number is {A[min_index]} at index {min_index}")

    else:
        # Predefined arrays to test the function
        arrays = {   
            "A3": [44, 63, 77, 17, 20, 99, 84, 6, 39, 52],
            "A4": [52, 84, 6, 39, 20, 77, 17, 99, 44, 63],
            "A5": [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
        }
        
        # Loop through predefined arrays and find the minimum element
        for name, arr in arrays.items():
            print(f"\nFinding minimum number in {name}")
            min_index = Min(arr, 0, len(arr) - 1)
            print(f"The minimum number in {name} is {arr[min_index]} at index {min_index}")

except ValueError:
    print("Invalid Input! Please enter integers only.")




