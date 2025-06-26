def sum_of_subarray_sums(A):
    total_sum = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            subarray_sum = sum(A[i:j+1])
            total_sum += subarray_sum
    return total_sum

# Sample Input
A = [1, 2, 3]

# Output
print(sum_of_subarray_sums(A))