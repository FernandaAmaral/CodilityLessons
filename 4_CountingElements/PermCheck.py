# Check whether array A is a permutation.

def solution(A):
    missing = 1
    A = sorted(A)

    for x in A:
        if(x == missing):
            missing += 1
        else:
            return 0

    return 1


A = [1, 2, 3, 5]
print(solution(A))
