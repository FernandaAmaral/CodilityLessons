# Find the missing element in a given permutation.

def solution(A):
    result = 0
    for i in range(1, len(A) + 2):
        result ^= i

    for i in A:
        result ^= i

    return result


A = [1, 2, 4, 5, 6, 7]
print(solution(A))
