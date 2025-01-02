
"""Develop one Python program to perform the Quicksort, but instead of sorting the
elements in ascending order (from the smallest to the largest), the elements are
sorted in the decrescent order (from the larger to the smallest).
Your program also have to compute and print at the end the number
of swaps performed and the number of recursive calls"""

def lomuto(A, left, right, swaps):
    p = A[right]
    i = left
    
    for j in range(left, right):
        if A[j] > p:  # Change comparison for descending order
            A[i], A[j] = A[j], A[i]
            swaps[0] += 1  # Count swaps
            i += 1
    A[i], A[right] = A[right], A[i]
    swaps[0] += 1  # Count swap for pivot placement
    return i # Return the position of the pivot after partitioning

def quicksort(A, left, right, swaps, calls):
    if left < right:
        calls[0] += 1  # Count recursive calls
        mid = lomuto(A, left, right, swaps)
        
        quicksort(A, left, mid - 1, swaps, calls)
        
        quicksort(A, mid + 1, right, swaps, calls)

#Arrays
A = [38, 21, 39, 60, -1, 10, 81, 23]
print("\nOriginal Array:", A)
swaps = [0]  # Initialize swap counter
calls = [0]  # Initialize call counter
quicksort(A, 0, len(A) - 1, swaps, calls)

print("Sorted array:", A)
print("Number of swaps:", swaps[0])
print("Number of recursive calls:", calls[0])


B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
print("\nOriginal Array:", B)
swaps = [0]  # Initialize swap counter
calls = [0]  # Initialize call counter
quicksort(B, 0, len(B) - 1, swaps, calls)

print("Sorted array:", B)
print("Number of swaps:", swaps[0])
print("Number of recursive calls:", calls[0])


C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
print("\nOriginal Array:", C)
swaps = [0]  # Initialize swap counter
calls = [0]  # Initialize call counter
quicksort(C, 0, len(C) - 1, swaps, calls)

print("Sorted array:", C)
print("Number of swaps:", swaps[0])
print("Number of recursive calls:", calls[0])



