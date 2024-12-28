def binSearch(A, start, end, k):
    mid = (start+ end)//2

    if start == 0 and end == len(A)-1 and start != end:
        # Print the entire array only for the initial call
        print(f"\nMain array: {A}")
        print(f"Searching for {k}")
    else:
        # For subsequent recursive calls, print only the subarray being searched
        print(f"\nSubarray: {A[start:end+1]}")
        
    print(f"Mid element for the array is: {A[mid]}")

     # Base case: If start index exceeds end index, the element is not found
    if (start > end):
        print("Subarray is empty, element not found")
        return None
    
    elif (A[mid] == k): # Check if the mid element is the target
        return mid
    
    elif (A[mid] < k): # For descending order: if mid element is less than the target, search left half
        return binSearch(A, start, mid-1, k)
    
    # For descending order: if mid element is greater than the target, search right half
    else:
        return binSearch(A, mid+1, end, k)

# Handling user input and testing the function
try:
    # Prompt the user to enter an array
    x = input("Enter an array of numbers seperated by spaces: ")

    if x.strip():
        # Convert input string to a list of integers
        A = list(map(int, x.split()))

        # Get the target number to search for
        k = int(input("Enter the number to search for: "))

        # Sort the array in descending order
        A.sort(reverse=True)
        print(f"Sorted array (descending): {A}")

         # Perform binary search
        result = binSearch(A, 0, len(A) -1, k)

        # Display the search result
        if result != None:
            print(f"{k} is at index {result}")
        else:
            print(f"{k} was not found in the list")
              
    else:
        # Test cases if no input is provided
        A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
        print(f"\nTesting on predefined array A1: {A1}")
        print(f"44 is at index {binSearch(A1, 0, len(A1) -1, 44)}")
        print(f"56 is at index {binSearch(A1, 0, len(A1) -1, 56)}")
        print(f"42 is at index {binSearch(A1, 0, len(A1) -1, 42)}")
              
        A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]
        print(f"\nTesting on predefined array A2: {A2}")
        print(f"-1 is at index {binSearch(A2, 0, len(A2) -1, -1)}")
        print(f"-7 is at index {binSearch(A2, 0, len(A2) -1, -7)}")

except ValueError:
    print("Invalid Input! Please enters integers only.")

