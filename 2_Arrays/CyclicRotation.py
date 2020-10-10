# Rotate an array to the right by a given number of steps.

def solution(A, K):
    N = len(A)
    new_A = [None] * N

    # If A is empty
    if(not N):
        return A

    # If K is bigger than array size, ignores full cycles
    if(K >= N):
        K = K % N

    for i in range(0, N):
        if(i + K < N):
            new_A[i+K] = A[i]
        else:
            new_A[K-(N-i)] = A[i]

    return new_A


A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
K = 0
print(solution(A, K))
