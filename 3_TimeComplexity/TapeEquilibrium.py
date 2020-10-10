# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

def solution(A):
    minimum = max(A) - min(A)
    start_sum = 0
    sum_A = sum(A)

    if(len(A) == 2):
        return minimum

    for i in range(0, len(A) - 1):
        start_sum += A[i]
        diff = abs(sum_A - 2*start_sum)
        if(diff < minimum):
            minimum = diff
    return minimum


A = [-10, -20, -30, -40, 100]
print(solution(A))
