def mergesort(A):
    if len(A)<= 1:
        print(f"Base case reached: {A}")
        return A
    else:
        mid = len(A)//2
        print(f"Splitting: {A} into {A[:mid]} and {A[mid:]}")
        left = mergesort(A[:mid])
        right = mergesort(A[mid:])
        merged = merge(left, right)
        print(f"Merging: {left} and {right} into {merged}\n")
        return merged

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


#Trace the Mergesort algorithm for the following arrays. Show to each recursive
#call the two input and output arrays

print("Tracing Array A:")
A = [38, 21, 39, 60, -1, 10, 81, 23]
result = mergesort(A)
print(f"Sorted A: {result}\n")

print("Tracing Array B:")
B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
result = mergesort(B)
print(f"Sorted B: {result}\n")

print("Tracing Array C:")
C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
result = mergesort(C)
print(f"Sorted C: {result}\n")
