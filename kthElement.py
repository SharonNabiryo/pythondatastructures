import random

def quickSelect(A, left, right, k):
    
    kth_element = k - 1  # Convert 1-based `k` to 0-based index
    p = A[right]
    i = left

    # Partition the array
    for j in range(left, right):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
            
    # Place the pivot in its correct position        
    A[i], A[right] = A[right], A[i]

    # Recursively narrow down to the kth smallest element
    if i > kth_element:
        return quickSelect(A, left, i-1, k)
    elif i < kth_element:
        return quickSelect(A, i+1, right, k)
    else:
        return A[i]


def main():
    # Generate a random array of 1000 elements
    n = 1000
    A = [random.randint(1, 10000) for _ in range(n)]
    
    # Ask the user for the value of k
    while True:
        try:
            k = int(input(f"Enter the value of k (1 <= k <= {n}): "))
            if 1 <= k <= n:
                break
            else:
                print(f"Please enter a number between 1 and {n}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Find the k-th smallest element using QuickSelect
    result = quickSelect(A, 0, len(A) - 1, k)
    
    # Display the result
    print(f"The {k}th smallest element in the array is: {result}")


# Run the program
if __name__ == "__main__":
    main()













    



