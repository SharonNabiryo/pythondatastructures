def lomuto(A, left, right):
    print(f"Original Array: {A}")
    print("")
    p = A[right]
    i = left
    
    for j in range(left, right):
        print(f"i (A[{i}]) = {A[i]}")
        print(f"j (A[{j}]) = {A[j]}")
        print(f"Elements yet to compare: {A[j: right]}")
        print("")
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            
            print(f"{A[i]} has now been swapped with {A[j]} ")
            print("")
            i += 1
            
            
    A[i], A[right] = A[right], A[i]
    print(f"Pivot swapped: A[{i}] = {A[i]} with A[{right}] = {A[right]}")
    
    print("")
    return i

#A = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
A = [198, 62, 127]

pvt = lomuto(A, 0, len(A)-1)

print(f"Lomuto with pivot at {pvt}: {A[pvt]}")
print(f"Array of elements lesser than pivot: {A[:pvt]}")
print(f"Array of elements greater than pivot: {A[pvt+1:]}")
print(f"Final Array: {A}")


"""In your trace,
write down to each change in either i or j,
stating: the values of i and j,
swaps made,
and elements divided into lesser than the pivot,
greater than the pivot,
and yet to compare."""

