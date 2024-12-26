"""Trace the recursive array sum algorithm for the following arrays.
Show to each recursive call the input array,
the returned value,
and the number of sums executed.
At the end of the trace, present the total number of sums executed (the
total of sums of all recursive calls"""

def arraySum(A, start, end):
    
    
    if (start == end):
        print(f"Base case: A[{start}:{end + 1}] = {A[start:end + 1]}, "
              f"\nReturned value: {A[start]}, "
              f"\nAdditions: 0\n")
        
        return A[start], 0
    
    else:
        mid = (start+end)//2
        left_sum, left_additions = arraySum(A, start, mid)
        right_sum, right_additions = arraySum(A, mid+1, end)
        
        
        total = left_sum + right_sum
        current_additions = 1
        additions = left_additions + right_additions + current_additions 

        print(f"Recursive call: A[{start}:{end + 1}] = {A[start:end + 1]}, "
          f"\nReturned value: {total}, "
            f"\nAdditions: {current_additions}\n")
        
        return total, additions


    
#print("Tracing Array A")
#A = [38, 21, 39, 60, -1, 10, 81, 23]
#result, additions = arraySum(A, 0, len(A)-1)
#print(f"\nSum of A: {result}, Total additions: {additions}\n") 

print("Tracing Array B")
B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
result, additions = arraySum(B, 0, len(B)-1)
print(f"\nSum of B: {result}, Total additions: {additions}\n")

#print("Tracing Array C")
#C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
#result, additions = arraySum(C, 0, len(C)-1)
#print(f"\nSum of C: {result}, Total additions: {additions}") 


"""def arraySum(A, start, end):
    if (start == end):
        return A[start]
    else:
        mid = (start+end)//2
        return arraySum(A, start, mid) + arraySum(A, mid+1, end)

A = [38, 21, 39, 60, -1, 10, 81, 23]
result = arraySum(A, 0, len(A)-1)
print(result) 

B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
result = arraySum(B, 0, len(B)-1)
print(result)

C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
result = arraySum(C, 0, len(C)-1)
print(result)""" 

